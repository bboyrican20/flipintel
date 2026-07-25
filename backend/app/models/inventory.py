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


    purchase_date = Column(
        DateTime,
        default=datetime.utcnow
    )


    status = Column(
        String,
        default="PURCHASED"
    )


    notes = Column(
        String,
        nullable=True
    )


    #
    # PRODUCT RELATIONSHIP
    #

    product = relationship(
        "Product",
        back_populates="inventory"
    )