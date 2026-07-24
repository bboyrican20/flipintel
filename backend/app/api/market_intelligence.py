from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.market_data import MarketData

from app.services.market_intelligence import MarketIntelligence


router = APIRouter(
    prefix="/market-intelligence",
    tags=["Market Intelligence"]
)


@router.get("/{product_id}")
def get_market_intelligence(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = (
        db.query(Product)
        .filter(Product.id == product_id)
        .first()
    )


    if product is None:

        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )



    market_records = (
        db.query(MarketData)
        .filter(
            MarketData.product_id == product_id
        )
        .all()
    )



    market_data = []


    for item in market_records:

        market_data.append({

            "price": item.price,

            "sold_count": item.sold_count,

            "source": item.source,

            "condition": item.condition

        })



    engine = MarketIntelligence()



    intelligence = engine.analyze_market(
        product.name,
        market_data
    )


    return {

        "product_id": product.id,

        "product": product.name,

        "brand": product.brand,

        "current_buy_price": product.buy_price,

        "intelligence": intelligence

    }