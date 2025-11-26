from pydantic import BaseModel
from typing import List


# Pydantic model for Mobile Accessory
class MobileAccessory(BaseModel):
    id: int
    phone_model: str
    name: str
    price: int
    currency: str
    on_sale: bool
    image_uri: str
    description: str


# Pydantic model for paginated response
class PaginatedResponse(BaseModel):
    data: List[MobileAccessory]
    total: int
