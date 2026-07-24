from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.market_data import MarketData


router = APIRouter(
    prefix="/market-data",
    tags=["Market Data"]
)


@router.post("/")
def create_market_data(
    data: dict,
    db: Session = Depends(get_db)
):

    market_entry = MarketData(

        product_id=data["product_id"],

        source=data["source"],

        marketplace=data.get("marketplace"),

        price=data.get("price"),

        condition=data.get("condition"),

        sold_count=data.get("sold_count"),

        average_price=data.get("average_price")

    )

    db.add(market_entry)

    db.commit()

    db.refresh(market_entry)


    return {

        "id": market_entry.id,

        "message": "Market data saved",

        "product_id": market_entry.product_id

    }