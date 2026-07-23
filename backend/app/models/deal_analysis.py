from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from datetime import datetime

from app.db.database import Base


class DealAnalysis(Base):
    __tablename__ = "deal_analysis"

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

    flipintel_score = Column(
        Integer,
        nullable=False
    )

    recommendation = Column(
        String,
        nullable=False
    )

    reasons = Column(
        String,
        nullable=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )