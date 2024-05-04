import datetime
import fastapi as fastapi
import sqlalchemy.orm as _orm
from sqlalchemy.orm import attributes as _attributes
import schema
import utils
from typing import List
app = fastapi.FastAPI()

@app.post("/create/books")
async def create_books(
    book: schema.BookBase, db: _orm.Session = fastapi.Depends(utils.get_db)
):
    """
    Creates a new book in the database

    Parameters
    ----------
    book : schema.BookBase
        The book to be created
    db : Session
        The database session

    Returns
    -------
    dict
        A dictionary containing a success message and the created book

    """
   
    # Check if any required field is missing
    if not any([book.title, book.author, book.isbn, book.year]):
        raise fastapi.HTTPException(status_code=400, detail="All fields (title, author, ISBN, year) are required")

    # Validate the year
    current_year = datetime.datetime.now().year
    if book.year < 1000 or book.year > current_year:
        raise fastapi.HTTPException(status_code=400, detail="Invalid year")
    
    # Check if a book with the same ISBN already exists
    db_book = await utils.get_books_by_isbn(isbn=book.isbn, db=db)
    if db_book:
        raise fastapi.HTTPException(status_code=400, detail="Book with the same ISBN already registered")
    
    if len(book.isbn) < 10 or len(book.isbn) > 13:
        raise fastapi.HTTPException(status_code=400, detail="ISBN must be at least 10 characters long or 13 characters long")
    # Create the book
    created_book = await utils.create_books(db=db, book=book)

    if isinstance(created_book, str):
        # If creation failed, return an error response
        return fastapi.Response(content=created_book, status_code=400)
    else:
        # If creation succeeded, return a success response
        return {"message": "Book created successfully", "book": created_book}


@app.get("/get/books/", response_model=List[schema.BookResponse])
async def get_all_books(db: _orm.Session = fastapi.Depends(utils.get_db)):
    """
    Get all books from the database

    Parameters
    ----------
    db : Session
        The database session

    Returns
    -------
    list
        A list of books

    """

    all_books = await utils.get_all_books(db=db)
    
    if not all_books:
        return {"error": "Oops! You have no books yet. Please go ahead and create a new book."}
    else:
        return all_books
    
@app.get("/get/books/{id}", response_model=schema.BookResponse)
async def get_book_by_id(id: int, db: _orm.Session = fastapi.Depends(utils.get_db)):
    """
    Get a book by its ID

    Parameters
    ----------
    id : int
        The ID of the book
    db : Session
        The database session

    Returns
    -------
    dict
        A dictionary containing the book

    """
    # Check if the book exists
    book = await utils.get_books_by_id(id=id, db=db)
    # Return an error response if the book does not exist
    if not book:
        raise fastapi.HTTPException(status_code=404, detail=f"Book with specified id not found.please enter a valid id")

    else:
        return book
    
@app.put("/update/books/{id}", response_model=schema.BookResponse)
async def update_book_by_id(id: int, book: schema.BookUpdate, db: _orm.Session = fastapi.Depends(utils.get_db)):
    """
    Update a book by its ID

    Parameters
    ----------
    id : int
        The ID of the book
    book : schema.BookBase
        The updated book
    db : Session
        The database session

    Returns
    -------
    dict
        A dictionary containing the updated book

    """
    # Check if the book exists
    db_book = await utils.update_books_by_id(id=id, db=db, book=book)

    # Return an error response if the book does not exist
    if not db_book:
        raise fastapi.HTTPException(status_code=404, detail=f"Book with specified id not found. Please enter a valid id")

    

    # Perform individual validation checks for each field
    if not isinstance(book.title, str):
        raise fastapi.HTTPException(status_code=400, detail="Title must be a string")
    if not isinstance(book.author, str):
        raise fastapi.HTTPException(status_code=400, detail="Author must be a string")
    if not isinstance(book.year, int):
        raise fastapi.HTTPException(status_code=400, detail="Year must be an integer")
    if not isinstance(book.isbn, str):
        raise fastapi.HTTPException(status_code=400, detail="ISBN must be a string")
    if not (1000 <= book.year <= datetime.datetime.now().year):
        raise fastapi.HTTPException(status_code=400, detail="Invalid year")

    if db_book == book:
      raise fastapi.HTTPException(status_code=400, detail="No changes detected. Please provide updated information")

    if len(book.isbn) < 10 or len(book.isbn) > 13:
        raise fastapi.HTTPException(status_code=400, detail="ISBN must be at least 10 characters long or 13 characters long")
    if db_book.isbn != book.isbn:
        db_book.isbn = book.isbn

    if db_book.title != book.title:
        db_book.title = book.title

    if db_book.author != book.author:
        db_book.author = book.author

    if db_book.year != book.year:
        db_book.year = book.year
    

    

        
        
    return db_book


@app.delete("/delete/books/{id}")
async def delete_book_by_id(id: int, db: _orm.Session = fastapi.Depends(utils.get_db)):
    """
    Delete a book by its ID

    Parameters
    ----------
    id : int
        The ID of the book
    db : Session
        The database session

    Returns
    -------
    dict
        A dictionary containing the deleted book

    """
    # Check if the book exists
    db_book = await utils.get_books_by_id(id=id, db=db)
    # Return an error response if the book does not exist
    if not db_book:
        raise fastapi.HTTPException(status_code=404, detail=f"Book with specified id not found. Please enter a valid id")

    # Delete the book
    db.delete(db_book)
    db.commit()
    return {"message": "Book deleted successfully"}