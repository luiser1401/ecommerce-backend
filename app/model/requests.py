import datetime
import uuid

from pydantic import BaseModel, ConfigDict, UUID4, Field


class EcomRequest(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True
    )

    request_id: UUID4 = Field(
        default_factory=uuid.uuid4
    )

    name: str
    description: str
    price: float
    discount_price: float
    stock_quantity: int
    sku: str
    image_ur: str
    category: str
    brand: str
    weight: float
    dimensions: str  # format: LxWxH in cm
    is_active: bool
    is_featured: bool
    created_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
    updated_at: datetime.datetime = Field(default_factory=datetime.datetime.utcnow)
