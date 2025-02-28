from pydantic import BaseModel
from typing import List, Optional

# User schemas
class UserBase(BaseModel):
    username: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# Movie schema
class MovieBase(BaseModel):
    title: str
    genre: str
    year: int

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Review schema
class ReviewCreate(BaseModel):
    rating: int
    comment: Optional[str] = None

class Review(ReviewCreate):
    id: int
    movie_id: int

    class Config:
        orm_mode = True

# Movie response schema (for the `/movies` endpoint)
class MovieListResponse(BaseModel):
    movies: List[Movie]

    class Config:
        orm_mode = True

# Token schema
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None