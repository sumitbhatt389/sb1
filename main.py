import os
from admin import create_admin
from fastapi import FastAPI, Depends, HTTPException, Request, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models
import schemas
import auth 
from typing import List
from logger import logger
from fastapi.responses import JSONResponse
from models import User, Movie, Review
from schemas import MovieCreate, UserBase
import logging
from auth import get_current_user
# from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi


app = FastAPI(debug=True,
              swagger_ui_oauth2_redirect_url="/docs/oauth2-redirect",
              title="Movie Rating System API",
              description="A FastAPI project with authentication using OAuth2 Bearer Tokens",
              version="1.0",
              docs_url="/docs",  # Ensures Swagger is accessible at /docs
              redoc_url="/redoc"
              )

# import models
# import schemas
# import auth 
# from fastapi.security import OAuth2PasswordBearer
# from sqlalchemy.orm import Session
admin = create_admin(app)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))

logger = logging.getLogger(__name__)

# OAuth2 scheme for authentication
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login", auto_error=False)

# Define the database URL
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

# Database setup
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["*"],  # Allow all origins during development (change this in production)
#     allow_credentials=True,
#     allow_methods=["*"],  # Allow all HTTP methods
#     allow_headers=["*"],  # Allow all headers
# )

def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema  # Prevent recursion

    openapi_schema = get_openapi(
        title="Movie Rating System",
        version="1.0.0",
        description="API for managing movie ratings and reviews",
        routes=app.routes,
    )

    if "components" not in openapi_schema:
        openapi_schema["components"] = {}

    openapi_schema["components"]["securitySchemes"] = {
        "OAuth2PasswordBearer": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"OAuth2PasswordBearer": []}]

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

@app.exception_handler(Exception)
async def global_exception_handler(request: Request, exc: Exception):
    logger.error(f"Unhandled exception: {exc}")
    return JSONResponse(status_code=500, content={"message": "Internal Server Error"})

@app.middleware("http")
async def catch_exceptions_middleware(request: Request, call_next):
    try:
        return await call_next(request)
    except Exception as e:
        logger.error(f"Unhandled Exception: {e}")
        return JSONResponse(status_code=500, content={"error": str(e)})

@app.get("/secure-endpoint")
async def secure_data(token: str = Depends(oauth2_scheme)):
    # Token verification logic
    if not token:
        raise HTTPException(status_code=401, detail="Token required")
    return {"message": "Secure data accessed"}

@app.get("/")
async def hello_world():
    return {"message": "Movie Rating System API"}

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/api/users", response_model=List[schemas.User])
async def get_user_list(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    try:
        users = db.query(User).all()
        logger.info(f"Fetched {len(users)} users.")
        return users
    except Exception as e:
        logger.error(f"Error fetching users: {e}")
        raise HTTPException(status_code=500, detail="Internal Server Error")

@app.post("/register", response_model=schemas.User)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username already taken")
    hashed_password = auth.get_password_hash(user.password)
    db_user = models.User(username=user.username, hashed_password=hashed_password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.post("/login", response_model=schemas.Token)
async def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    access_token = auth.create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# Function to get the current user

@app.post("/movies/", response_model=schemas.Movie)
async def create_movie(movie: schemas.MovieCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    
    db_movie = models.Movie(id=movie.id, title=movie.title, genre=movie.genre, year=movie.year, user_id=current_user.id)
    db.add(db_movie)
    db.commit()
    db.refresh(db_movie)
    return db_movie

@app.get("/movies/{movie_id}", response_model=schemas.Movie)
async def get_movie(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")
    return db_movie

@app.post("/movies/{movie_id}/reviews", response_model=schemas.Review)
async def create_review(movie_id: int, review: schemas.ReviewCreate, db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    db_review = models.Review(rating=review.rating, comment=review.comment, movie_id=movie_id, user_id=current_user.id)
    db.add(db_review)
    db.commit()
    db.refresh(db_review)
    return db_review

@app.get("/movies/{movie_id}/reviews", response_model=List[schemas.Review])
async def get_reviews(movie_id: int, db: Session = Depends(get_db)):
    db_movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if db_movie is None:
        raise HTTPException(status_code=404, detail="Movie not found")

    reviews = db.query(models.Review).filter(models.Review.movie_id == movie_id).all()
    return reviews

# Create Category (POST)
@app.post("/categories/", response_model=schemas.CategoryOut)
def create_category(category: schemas.CategoryCreate, movie_id: int, db: Session = Depends(get_db)):
    # Check if movie exists
    movie = db.query(models.Movie).filter(models.Movie.id == movie_id).first()
    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    # Create the category
    db_category = models.Category(name=category.name)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    # Assign the category to the movie
    movie.category_id = db_category.id
    db.commit()

    return db_category

# Get All Categories (GET)
@app.get("/categories/", response_model=list[schemas.CategoryOut])
def get_categories(db: Session = Depends(get_db)):
    return db.query(models.Category).all()
