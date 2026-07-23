from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.product import Product
from app.services.deal_analyzer import analyze_product


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


@router.get("/{product_id}")
def analyze_deal(
    product_id: int,
    db: Session = Depends(get_db)
):
    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )

    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    result = analyze_product(product)

    return {
        "product": product.name,
        "analysis": result
    }