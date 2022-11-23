# import sys

# print('Hello, World!')

# print('The sum of 2 and 3 is 5.')

# sum_1 = 4 + 10

# print(f'The sum is {sum_1}.')
import sqlalchemy
import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, Boolean, Column, Integer, String, ForeignKey
from sqlalchemy import schema
from sqlalchemy.orm import declarative_base, relationship, joinedload
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from typing import Any, List
# from sqlalchemy_uti


DB_ENGINE = "postgresql"
DB_USERNAME = "postgres"
DB_PASSWORD = "postgres"
DB_HOST = "10.192.250.55"
DB_PORT = "5432"
DB_DATABASE = "mydatabase2"
DB_SCHEMA = "myschema2"
# Initializing Application && DB  ( CREATE DATABASE IF NOT EXISTS)
engine = create_engine(
    f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}")


# existing_databases = engine.execute("SHOW DATABASES;")

# existing_databases = [d[0] for d in existing_databases]
# Create database if not exists
# if DB_DATABASE not in existing_databases:
try:
    with engine.connect() as conn:
        conn.execute("commit")  # close open transaction session
        conn.execute(f"CREATE DATABASE {DB_DATABASE};")
except:
    pass


# Make the engine
# postgresql://postgres:postgres@10.192.250.55:5432/test_bt
# postgresql://postgres:postgres@database-free-tier-audit.c0ypdd525au7.us-east-1.rds.amazonaws.com:5432/test_bt
engine = create_engine(
    f"{DB_ENGINE}://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}?options=-csearch_path={DB_SCHEMA}", future=True, echo=True)
# engine.execute
engine.begin()
# if not engine.dialect. has_schema(engine, DB_SCHEMA):
#     pass

# engine.execute(schema.CreateSchema(DB_SCHEMA, if_not_exists=True))
# connect_args={"check_same_thread": False}
with engine.connect() as connection:
    # connection.execute(f"CREATE SCHEMA IF NOT EXISTS {DB_SCHEMA}; ")
    connection.execute(schema.CreateSchema(DB_SCHEMA, if_not_exists=True))
    connection.commit()
    # connection
    # connection.execute("commit")
    # connection.execute(f'CREATE SCHEMA IF NOT EXISTS {DB_SCHEMA}')

# def get_db():
#     db = Session(bind=engine)
#     try:
#         yield db
#     finally:
#         db.close()

# my_db = get_db()
# if not my_db :
#     pass

# # Make the DeclarativeMeta
Base = declarative_base()

# Declare Classes / Tables


class BookAuthor(Base):
    __tablename__ = 'book_authors'
    book_id = Column(ForeignKey('books.id'), primary_key=True)
    author_id = Column(ForeignKey('authors.id'), primary_key=True)
    blurb = Column(String, nullable=False)
    book = relationship("Book", back_populates="authors")
    author = relationship("Author")


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    authors = relationship("BookAuthor")


class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    books = relationship("BookAuthor", back_populates="author")


# Create the tables in the database
Base.metadata.create_all(engine)


# Insert data
if True:
    with Session(bind=engine) as session:
        book1 = Book(title="Harry Potter")
        book2 = Book(title="GOT")

        author1 = Author(name="JK Roll")
        author2 = Author(name="AR Al")
        author3 = Author(name="LEF")

        session.add_all([book1, book2, author1, author2, author3])
        session.commit()

        book_author1 = BookAuthor(
            book_id=book1.id, author_id=author1.id, blurb="Blue wrote chapter 1")
        book_author2 = BookAuthor(
            book_id=book1.id, author_id=author2.id, blurb="Chip wrote chapter 2")
        book_author3 = BookAuthor(
            book_id=book2.id, author_id=author1.id, blurb="Blue wrote chapters 1-3")
        book_author4 = BookAuthor(
            book_id=book2.id, author_id=author3.id, blurb="Alyssa wrote chapter 4")

        session.add_all([book_author1, book_author2,
                        book_author3, book_author4])
        session.commit()


class RelatedBookSchema(BaseModel):
    id: int
    title: str

    class Config:
        orm_mode = True


class AuthorBookSchema(BaseModel):
    blurb: str
    book: Optional[RelatedBookSchema]

    class Config:
        orm_mode = True


class AuthorSchema(BaseModel):
    id: int
    name: str
    books: List[AuthorBookSchema]

    def dict(self, **kwargs):
        data = super(AuthorSchema, self).dict(**kwargs)

        for b in data['books']:
            b['id'] = b['book']['id']
            b['title'] = b['book']['title']
            del b['book']

        return data

    class Config:
        orm_mode = True


class RelatedAuthorSchema(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class BookAuthorSchema(BaseModel):
    blurb: str
    author: Optional[RelatedAuthorSchema]

    class Config:
        orm_mode = True


class BookSchema(BaseModel):
    id: int
    title: str
    authors: List[BookAuthorSchema]

    def dict(self, **kwargs):
        data = super(BookSchema, self).dict(**kwargs)

        for a in data['authors']:
            a['id'] = a['author']['id']
            a['name'] = a['author']['name']
            del a['author']

        return data

    class Config:
        orm_mode = True


app = FastAPI(title="Bookipedia")


def get_db():
    db = Session(bind=engine)
    try:
        yield db
    finally:
        db.close()


@app.get("/books/{id}", response_model=BookSchema)
async def get_book(id: int, db: Session = Depends(get_db)):
    db_book = db.query(Book).options(
        joinedload(Book.authors).options(
            joinedload(BookAuthor.author)
        )
    ).where(Book.id == id).one()
    return db_book


@app.get("/books", response_model=List[BookSchema])
async def get_books(db: Session = Depends(get_db)):
    db_books = db.query(Book).options(
        joinedload(Book.authors).options(
            joinedload(BookAuthor.author)
        )
    ).all()
    return db_books


@app.get("/authors/{id}", response_model=AuthorSchema)
async def get_author(id: int, db: Session = Depends(get_db)):
    db_author = db.query(Author).options(
        joinedload(Author.books).options(
            joinedload(BookAuthor.book)
        )
    ).where(Author.id == id).one()
    return db_author


@app.get("/authors", response_model=List[AuthorSchema])
def get_authors(db: Session = Depends(get_db)):
    db_authors = db.query(Author).options(
        joinedload(Author.books).options(
            joinedload(BookAuthor.book)
        )
    ).all()
    return db_authors


# print(get_authors())
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
