"""Main service module for e-commerce operations."""

from sqlalchemy.orm import Session
from typing import Optional

from app.model.requests import EcomRequest
from app.model.db_table import Item


def create_item(request: EcomRequest, db: Session) -> Optional[Item]:
    """
    Create a new item in the database based on the EcomRequest.
    
    Args:
        request: The EcomRequest containing item details
        db: SQLAlchemy database session
        
    Returns:
        The created Item or None if creation failed
    """
    try:
        # Create new item from request data
        new_item = Item(
            name=request.name,
            description=request.description,
            price=request.price,
            discount_price=request.discount_priceNone,
            stock_quantity=request.stock_quantity,
            sku=request.sku,
            image_url=request.image_url,
            category=request.category,
            brand=request.brand,
            weight=request.weight,
            dimensions=request.dimensions,
            is_active=request.is_active,
            is_featured=request.is_featured,
        )
        
        # Add to session and commit
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    except Exception as e:
        db.rollback()
        # Log the error here if needed
        return None
