"""Repository for Item database operations."""

from sqlalchemy.orm import Session
from typing import Optional

from app.model.db_table import Item
from app.exceptions import EcommerceBackendException


def write_to_db(db: Session, item: Item) -> Optional[Item]:
    """
    Write an item to the database.
    
    Args:
        db: SQLAlchemy database session
        item: The Item object to persist
        
    Returns:
        The persisted Item or None if operation failed
    """
    try:
        db.add(item)
        db.commit()
        db.refresh(item)
        return item
    except Exception as e:
        db.rollback()
        # Log the error here if needed
        raise EcommerceBackendException(f"Failed to write item to database: {str(e)}")
