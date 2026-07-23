from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime

from app.db.database import Base


class Product(Base):

    __tablename__ = "products"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    name = Column(
        String,
        nullable=False
    )


    brand = Column(
        String,
        nullable=True
    )


    category = Column(
        String,
        nullable=True
    )


    sku = Column(
        String,
        nullable=True
    )


    upc = Column(
        String,
        nullable=True
    )


    barcode = Column(
        String,
        nullable=True
    )


    retailer = Column(
        String,
        nullable=False
    )


    url = Column(
        String,
        nullable=True
    )


    buy_price = Column(
        Float,
        nullable=False
    )


    sell_price = Column(
        Float,
        nullable=True
    )


    market_price = Column(
        Float,
        nullable=True
    )


    profit = Column(
        Float,
        nullable=True
    )


    roi = Column(
        Float,
        nullable=True
    )


    sales_velocity = Column(
        String,
        nullable=True
    )


    status = Column(
        String,
        default="active"
    )


    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    updated_at = Column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )