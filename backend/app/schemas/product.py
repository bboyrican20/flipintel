from pydantic import BaseModel
from typing import Optional


class ProductCreate(BaseModel):
    name: str
    sku: Optional[str] = None
    upc: Optional[str] = None

    retailer: str
    url: Optional[str] = None

    buy_price: float
    sell_price: Optional[float] = None


class ProductResponse(ProductCreate):
    id: int
    profit: Optional[float] = None
    roi: Optional[float] = None

    class Config:
        from_attributes = True