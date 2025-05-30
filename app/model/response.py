import datetime
from pydantic import BaseModel, Field


class EcomResponse(BaseModel):
    """Represents an item"""
    id: int
    name: str
    description: str
    price: float
    discount_price: float
    stock_quantity: int
    sku: str
    image_ur: str
    category: str
    brand: str
    weight: str
    dimensions: str  # format: LxWxH in cm
    is_active: bool
    is_featured: bool
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    response_created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)