from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from app.db.database import Base


class MarketData(Base):

    __tablename__ = "market_data"

    id = Column(Integer, primary_key=True, index=True)

    product_id = Column(
        Integer,
        ForeignKey("products.id"),
        nullable=False
    )

    source = Column(
        String,
        nullable=False
    )

    marketplace = Column(
        String,
        nullable=True
    )

    price = Column(
        Float,
        nullable=True
    )

    condition = Column(
        String,
        nullable=True
    )

    sold_count = Column(
        Integer,
        nullable=True
    )

    average_price = Column(
        Float,
        nullable=True
    )

    checked_at = Column(
        DateTime,
        default=datetime.utcnow
    )


    product = relationship(
        "Product",
        back_populates="market_data"
    )