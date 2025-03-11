import os
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker
from logger import logger
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
Base = declarative_base()
engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
#username=sumit
#password=sumit

DEBUG_MODE = os.getenv("DEBUG_MODE", "false").lower() == "true"

@event.listens_for(engine, "before_cursor_execute")
def before_cursor_execute(conn, cursor, statement, parameters, context, executemany):
    if DEBUG_MODE:
        logger.info(f"Executing query: {statement} with parameters: {parameters}")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
