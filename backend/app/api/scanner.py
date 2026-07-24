from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.market_data import MarketData
from app.models.scan_history import ScanHistory

from app.services.deal_analyzer import analyze_product
from app.services.barcode_lookup import lookup_barcode
from app.services.confidence_engine import calculate_confidence
from app.services.product_matcher import find_existing_product


router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)


@router.post("/barcode")
def scan_barcode(
    product_data: dict,
    db: Session = Depends(get_db)
):

    barcode = product_data["barcode"]


    lookup = lookup_barcode(barcode)


    if lookup is None:

        raise HTTPException(
            status_code=404,
            detail="Barcode not found"
        )



    buy_price = product_data["buy_price"]

    market_price = lookup["market_price"]


    profit = market_price - buy_price


    roi = (
        profit / buy_price * 100
        if buy_price > 0
        else 0
    )



    # CHECK IF PRODUCT ALREADY EXISTS

    product = find_existing_product(
        db,
        barcode=barcode
    )



    if product:


        product.buy_price = buy_price

        product.sell_price = market_price

        product.market_price = market_price

        product.profit = profit

        product.roi = roi

        product.retailer = product_data["retailer"]



        db.commit()

        db.refresh(product)



    else:


        product = Product(

            name=lookup["name"],

            brand=lookup["brand"],

            category=lookup["category"],

            barcode=barcode,

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




    market = MarketData(

        product_id=product.id,

        source="Barcode Lookup",

        marketplace="Internal Market Database",

        price=market_price,

        average_price=market_price,

        sold_count=25,

        condition="New"

    )


    db.add(market)

    db.commit()

    db.refresh(market)



    analysis = analyze_product(product)



    confidence = calculate_confidence(
        product,
        market
    )



    scan = ScanHistory(

        product_id=product.id,

        recommendation=analysis["recommendation"],

        flipintel_score=analysis["flipintel_score"],

        confidence_score=confidence["confidence"],

        profit=profit,

        roi=roi

    )


    db.add(scan)

    db.commit()

    db.refresh(scan)



    return {


        "product_id": product.id,

        "existing_product":
            True if product else False,


        "product": product.name,

        "brand": product.brand,

        "category": product.category,

        "market_price": market_price,

        "profit": profit,

        "roi": roi,

        "analysis": analysis,

        "confidence": confidence,

        "scan_history_id": scan.id

    }