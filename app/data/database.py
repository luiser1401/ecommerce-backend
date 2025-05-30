"""SQLAlchemy database module for data persistence."""

import os
from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# Database file path
DB_FILE = "ecommerce.db"
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), DB_FILE)
SQLALCHEMY_DATABASE_URL = f"sqlite:///{DB_PATH}"

# Create SQLAlchemy engine
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# Create session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()

def init_db() -> None:
    """Initialize the database with tables."""
    # Import models here to avoid circular imports
    # from app.data.models.product import Product
    # from app.data.models.user import User
    # from app.data.models.order import Order
    
    # Create all tables
    Base.metadata.create_all(bind=engine)

def get_db() -> Generator[Session, None, None]:
    """Get a database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
