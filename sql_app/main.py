from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app.utils import crud
from sql_app.models import models
from sql_app.schemas.schemas import User, UserCreate, Book, BookBase, BookCreate, User_Book, User_BookBase, User_BookCreate
from sql_app.database.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Online Library")


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=User, tags=["User"])
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=List[User], tags=["User"])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.get("/users/{user_id}", response_model=User, tags=["User"])
def read_user_by_id(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/books/{book_id}", response_model=Book, tags=["Book"])
def read_book_by_id(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id=book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@app.post("/books/", response_model=Book, tags=["Book"])
def create_book(book: BookBase, db: Session = Depends(get_db), ):
    return crud.create_book(db=db, book=book)


@app.get("/books/", response_model=List[Book], tags=["Book"])
def read_books(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    books = crud.get_books(db, skip=skip, limit=limit)
    return books



@app.post("/user_book/", response_model=User_Book, tags=["User_Book"])
def user_takes_book(u_b: User_BookBase, db: Session = Depends(get_db), ):
    return crud.user_takes_book(db=db, u_b=u_b)

