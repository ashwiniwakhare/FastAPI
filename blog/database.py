# Import required objects from SQLAlchemy for DB connection and ORM base class
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLite database URL - stored in current project directory as 'blog.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

# Create database engine
# Note: connect_args is required only for SQLite (threading issue workaround)
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal will be used to create DB session for each request
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)

# Base class for all ORM models (tables will inherit from this class)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()