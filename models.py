from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base
Base = declarative_base()

# SQLAlchemy User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    
    movies = relationship("Movie", back_populates="user", cascade="all, delete-orphan")

    # Relationship with Movies
    reviews = relationship("Review", back_populates="user")

# SQLAlchemy Movie model
class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    genre = Column(String)
    year = Column(Integer)

    # Foreign Key linking to User
    user_id = Column(Integer, ForeignKey("users.id"), nullable=True)
    user = relationship("User", back_populates="movies")

    # One-to-many relationship with Review
    reviews = relationship("Review", back_populates="movie")

# SQLAlchemy Review model
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String)

    # Foreign key to Movie
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)  # Make sure this exists!

    # Relationship to Movie
    movie = relationship("Movie", back_populates="reviews")
    user = relationship("User", back_populates="reviews")  # Make sure this relationship exists!