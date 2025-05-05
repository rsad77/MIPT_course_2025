from pydantic import BaseModel
from typing import Optional


# Модели для аутентификации
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None  # Именно этот класс отсутствовал


# Модели пользователей
class UserBase(BaseModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int

    class Config:
        from_attributes = True  # Замена orm_mode=True для Pydantic v2


# Модели книг
class BookBase(BaseModel):
    title: str
    author: str
    year: int
    genre_id: int


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int

    class Config:
        from_attributes = True