from sqlalchemy.orm import Session

from sql_app.models.models import User, Book, User_Book
from sql_app.schemas.schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    fake_hashed_password = user.password
    db_user = User(name=user.name, email=user.email, hashed_password=fake_hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_books(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Book).offset(skip).limit(limit).all()


def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()


def create_book(db: Session, book: Book):
    db_book = Book(title=book.title, author_id=book.author_id, genre_id=book.genre_id)
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def user_takes_book(db: Session, u_b: User_Book):
    db_u_b = User_Book(user_id=u_b.user_id, book_id=u_b.book_id)
    db.add(db_u_b)
    db.commit()
    db.refresh(db_u_b)
    return db_u_b
