from sqlalchemy.orm import Session
from models import Movie, Review
from schemas import MovieCreate, ReviewCreate

def get_movies(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Movie).offset(skip).limit(limit).all()

def create_movie(db: Session, movie: MovieCreate):
    db_movie = Movie(**movie.dict())
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

def get_reviews_for_movie(db: Session, movie_id: int, skip: int = 0, limit: int = 100):
    return db.query(Review).filter(Review.movie_id == movie_id).offset(skip).limit(limit).all()

def create_review_for_movie(db: Session, review: ReviewCreate, movie_id: int):
    db_review = Review(**review.dict(), movie_id=movie_id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review
