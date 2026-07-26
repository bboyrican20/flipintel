from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.services.deal_ai_engine import deal_ai_engine


router = APIRouter(
    prefix="/deal-ai",
    tags=["Deal AI"]
)


@router.get("/{product_id}")
def deal_ai(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:

        return {
            "error": "Product not found"
        }

    return deal_ai_engine.explain(
        product_id,
        db
    )