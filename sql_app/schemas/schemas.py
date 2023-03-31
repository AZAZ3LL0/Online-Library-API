from pydantic import BaseModel


class BookBase(BaseModel):
    title: str
    author_id: int
    genre_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str
    name: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    title: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class AuthorBase(BaseModel):
    name: str


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True


class User_BookBase(BaseModel):
    user_id: int
    book_id: int


class User_BookCreate(User_BookBase):
    pass


class User_Book(User_BookBase):
    id: int

    class Config:
        orm_mode = True
