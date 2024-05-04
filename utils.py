import database
import model 
import sqlalchemy.orm as _orm
import schema
from typing import Union



def create_database():
    return database.Base.metadata.create_all(bind=database.engine)




def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()



async def get_books_by_isbn(isbn:str, db: _orm.Session):
    return db.query(model.BookModel).filter(model.BookModel.isbn == isbn).first()



async def create_books(db: _orm.Session, book: schema.BookBase) -> Union[model.BookModel, str]:
    # Input validation
    if not isinstance(book.title, str):
        return {"error": "Title must be a string"}
    if not isinstance(book.author, str):
        return {"error": "Author must be a string"}
    if not isinstance(book.year, int):
        return {"error": "Year must be an integer"}
    if not isinstance(book.isbn, str):
        return {"error": "ISBN must be a string"}
    
    # Creating the BookModel object
    book_obj = model.BookModel(title=book.title, author=book.author, year=book.year, isbn=book.isbn)
    db.add(book_obj)
    db.commit()
    db.refresh(book_obj)
    return book_obj
async def get_all_books(db: _orm.Session):
    return db.query(model.BookModel).all()

async def get_books_by_id(id: int, db: _orm.Session):
    return db.query(model.BookModel).filter(model.BookModel.id == id).first()

async def update_books_by_id(id: int, book: schema.BookUpdate, db: _orm.Session):
    db_book = db.query(model.BookModel).filter(model.BookModel.id == id).first()
    if not db_book:
        return {"error": "Book not found"}
    db_book.title = book.title
    db_book.author = book.author
    db_book.year = book.year
    db_book.isbn = book.isbn
    db.commit()
    db.refresh(db_book)
    return db_book

create_database(); 