from pydantic import BaseModel
from typing import List, Optional

# User schemas
class UserCreate(BaseModel):
    username: str
    password: str
    id: Optional[int]

class User(BaseModel):
    id: Optional[int]
    username: str

    class Config:
        orm_mode = True

# Movie schemas
class MovieBase(BaseModel):
    title: str
    genre: str
    year: int
    id: Optional[int]

class MovieCreate(MovieBase):
    pass

class Movie(MovieBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

# Review schemas
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

# Token schemas
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None
class UserBase(BaseModel):
    id: int
    username: str
    is_admin: bool
    movies: Optional[List[str]] = []
    reviews: Optional[List[str]] = []

    class Config:
        orm_mode = True
        
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int
    class Config:
        orm_mode = True