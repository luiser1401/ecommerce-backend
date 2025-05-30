from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, Boolean, DateTime, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.data import Base

class Item(Base):
    __tablename__ = "items"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False)
    discount_price = Column(Float, nullable=True)
    stock_quantity = Column(Integer, default=0, nullable=False)
    sku = Column(String(50), unique=True, nullable=False)
    image_url = Column(String(255), nullable=True)
    category = Column(String(50), nullable=True, index=True)
    brand = Column(String(50), nullable=True, index=True)
    weight = Column(Float, nullable=True)  # in kg
    dimensions = Column(String(50), nullable=True)  # format: LxWxH in cm
    is_active = Column(Boolean, default=True)
    is_featured = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
