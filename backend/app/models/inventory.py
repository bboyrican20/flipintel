from sqlalchemy import Column, Integer, Float, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


class Inventory(Base):

    __tablename__ = "inventory"


    id = Column(
        Integer,
        primary_key=True,
        index=True
    )


    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )


    quantity = Column(
        Integer,
        default=1
    )


    purchase_price = Column(
        Float,
        nullable=False
    )


    expected_sale_price = Column(
        Float,
        nullable=True
    )


    projected_profit = Column(
        Float,
        nullable=True
    )


    status = Column(
        String,
        default="ACTIVE"
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


    product = relationship(
        "Product",
        back_populates="inventory"
    )