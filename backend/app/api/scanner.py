from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.product import Product
from app.services.deal_analyzer import analyze_product


router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)


@router.post("/analyze")
def scan_product(
    product_data: dict,
    db: Session = Depends(get_db)
):

    buy_price = product_data["buy_price"]
    market_price = product_data["market_price"]


    profit = market_price - buy_price

    roi = (
        profit / buy_price * 100
        if buy_price > 0
        else 0
    )


    product = Product(

        name=product_data["name"],

        brand=product_data.get("brand"),

        category=product_data.get("category"),

        barcode=product_data.get("barcode"),

        retailer=product_data["retailer"],

        buy_price=buy_price,

        sell_price=market_price,

        market_price=market_price,

        profit=profit,

        roi=roi,

        sales_velocity="HIGH"

    )


    db.add(product)

    db.commit()

    db.refresh(product)


    analysis = analyze_product(product)


    return {

        "product_id": product.id,

        "product": product.name,

        "profit": profit,

        "roi": roi,

        "flipintel_score":
            analysis["flipintel_score"],

        "recommendation":
            analysis["recommendation"],

        "reasons":
            analysis["reasons"]

    }