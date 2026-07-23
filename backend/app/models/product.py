from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)
    sku = Column(String, nullable=True)
    upc = Column(String, nullable=True)

    retailer = Column(String, nullable=False)
    url = Column(String, nullable=True)

    buy_price = Column(Float, nullable=False)
    sell_price = Column(Float, nullable=True)

    profit = Column(Float, nullable=True)
    roi = Column(Float, nullable=True)

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )