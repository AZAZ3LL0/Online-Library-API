from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from sql_app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String, index=True)
    is_active = Column(Boolean, default=True)

    user_book = relationship("User_Book", back_populates="users")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    genre_id = Column(Integer, ForeignKey("genre.id"))
    author_id = Column(Integer, ForeignKey("author.id"))

    genre = relationship("Genre", back_populates="books")
    author = relationship("Author", back_populates="books")
    user_book = relationship("User_Book", back_populates="books")


class Genre(Base):
    __tablename__ = "genre"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)

    books = relationship("Book", back_populates="genre")


class User_Book(Base):
    __tablename__ = "user_book"
    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(Integer, ForeignKey("users.id"))
    book_id = Column(Integer, ForeignKey("books.id"))

    users = relationship("User", back_populates="user_book")
    books = relationship("Book", back_populates="user_book")


class Author(Base):
    __tablename__ = "author"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)

    books = relationship("Book", back_populates="author")
