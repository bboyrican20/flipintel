from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from app.db.database import Base


class ScanHistory(Base):

    __tablename__ = "scan_history"


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


    recommendation = Column(
        String,
        nullable=False
    )


    flipintel_score = Column(
        Integer,
        nullable=False
    )


    confidence_score = Column(
        Integer,
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


    scanned_at = Column(
        DateTime,
        default=datetime.utcnow
    )