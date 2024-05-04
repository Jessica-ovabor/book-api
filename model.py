import datetime as datetime
import sqlalchemy as sqlalchemy
import sqlalchemy.orm as _orm
import database 


class BookModel(database.Base):
    __tablename__ = 'books'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    title = sqlalchemy.Column(sqlalchemy.String(255))
    author = sqlalchemy.Column(sqlalchemy.String(255))
    year = sqlalchemy.Column(sqlalchemy.Integer)
    isbn = sqlalchemy.Column(sqlalchemy.String(255))
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    updated_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)

    def __repr__(self):
        return f'<Book {self.name}>'
    