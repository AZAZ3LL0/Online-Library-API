from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author: str | None = None


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    name: str
    password: str


class User(UserBase):
    id: int
    is_active: bool
    books: list[Book] = []

    class Config:
        orm_mode = True
