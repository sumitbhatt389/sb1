from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from database import Base, engine

Base = declarative_base()

# SQLAlchemy User model
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    is_admin = Column(Boolean, default=False)

    # Relationships
    movies = relationship("Movie", back_populates="user", cascade="all, delete-orphan")
    reviews = relationship("Review", back_populates="user")

    def __str__(self):
        return self.username

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, index=True)
    movies = relationship("Movie", back_populates="category")

    def __str__(self):
        return self.name

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
    
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="movies")
    
    def __str__(self):
        return self.title

    
# SQLAlchemy Review model
class Review(Base):
    __tablename__ = "reviews"
    id = Column(Integer, primary_key=True, index=True)
    rating = Column(Integer)
    comment = Column(String)

    # Foreign Keys to Movie and User
    movie_id = Column(Integer, ForeignKey("movies.id"))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    # Relationships
    user = relationship("User", back_populates="reviews")
    movie = relationship("Movie", back_populates="reviews")

    def __str__(self):
        return f"{self.rating}/10 - {self.comment}" if self.comment else "No Comment"
    
Base.metadata.create_all(engine)
