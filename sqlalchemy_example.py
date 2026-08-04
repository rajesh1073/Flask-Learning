# pip install sqlalcemy

import sqlalchemy
import os

os.getcwd()

"""
Connection string :
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="EmployeeManagement"
)
"""

from sqlalchemy import create_engine, text
from sqlalchemy.exc import OperationalError

# Update these values to match your MySQL server configuration
DB_USER = "root"
DB_PASSWORD = "77468"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "EmployeeManagement"


def get_database_url(database_name: str | None = None) -> str:
    if database_name:
        return f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{database_name}"
    return f"mysql+mysqlconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/"


def ensure_database_exists() -> None:
    engine = create_engine(get_database_url(), pool_pre_ping=True)
    try:
        with engine.connect() as conn:
            conn.execute(text(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`"))
            conn.commit()
    finally:
        engine.dispose()


ensure_database_exists()

database_URL = get_database_url(DB_NAME)
engine = create_engine(database_URL, pool_pre_ping=True)

from sqlalchemy.orm import DeclarativeBase, mapped_column, relationship
from sqlalchemy import Integer, String, Float, ForeignKey


class Base(DeclarativeBase):
    pass


class Author(Base):
    __tablename__ = "authors"

    autid = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(50), nullable=False)
    age = mapped_column(Integer)

    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    bookid = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String(50), nullable=False)
    price = mapped_column(Float)
    autid = mapped_column(Integer, ForeignKey("authors.autid"))

    author = relationship("Author", back_populates="books")


# Create Tables
Base.metadata.create_all(engine)


from sqlalchemy.orm import Session

# Insert First Record
with Session(engine) as session:
    aut1 = Author(name="JK Rowling", age=50)

    book1 = Book(
        name="Harry Potter: chamber of sectres",
        price=6.6,
        autid=1
    )

    session.add_all([aut1, book1])
    session.commit()


# Insert Second Record
with Session(engine) as session:
    aut1 = Author(name="George RR Matin", age=60)

    book1 = Book(
        name="Harry Potter: Philosphers stone",
        price=6.6,
        autid=1
    )

    session.add_all([aut1, book1])
    session.commit()


# Read All Authors
with Session(engine) as session:
    res = session.query(Author).all()
    print(res)


# Convert Authors to Dictionary
with Session(engine) as session:
    res = session.query(Author).all()

    authors_list = [
        {
            column.name: getattr(author, column.name)
            for column in Author.__table__.columns
        }
        for author in res
    ]

    print(authors_list)


# Update Book Price
with Session(engine) as session:
    obj = session.query(Book).filter(Book.bookid == 2).first()
    obj.price = 7.7
    session.commit()


# Read Single Book
with Session(engine) as session:
    obj = session.query(Book).filter(Book.bookid == 2).first()

    book_dict = {
        "bookid": obj.bookid,
        "name": obj.name,
        "price": obj.price,
        "autid": obj.autid
    }

    print(book_dict)


# Filter By
with Session(engine) as session:
    obj = session.query(Book).filter_by(bookid=2).first()
    print(obj)


# Get Book
with Session(engine) as session:
    obj = session.get(Book, 2)
    print(obj)


# Get Book as Dictionary
with Session(engine) as session:
    obj = session.get(Book, 2)

    book_dict = {
        "bookid": obj.bookid,
        "name": obj.name,
        "price": obj.price,
        "autid": obj.autid
    }

    print(book_dict)


# Delete Author
with Session(engine) as session:
    obj = session.get(Author, 2)

    if obj:
        session.delete(obj)
        session.commit()


# Count Books
with Session(engine) as session:
    count = session.query(Book).count()
    print("Total Books:", count)


# Add New Author
author = Author(name="John", age=40)

with Session(engine) as session:
    session.add(author)
    session.commit()


# Get Book Name
with Session(engine) as session:
    obj = session.get(Book, 1)

    if obj:
        print(obj.name)


# Update Book Price
with Session(engine) as session:
    obj = session.get(Book, 1)

    if obj:
        obj.price = 999
        session.commit()


# Delete Book
with Session(engine) as session:
    obj = session.get(Book, 1)

    if obj:
        session.delete(obj)
        session.commit()


# SQLAlchemy 2.0 Style Query
from sqlalchemy import select

with Session(engine) as session:
    books = session.scalars(select(Book)).all()
    print(books)