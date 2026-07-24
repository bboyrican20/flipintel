from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.market_data import MarketData
from app.models.scan_history import ScanHistory

from app.services.barcode_lookup import lookup_barcode
from app.services.confidence_engine import calculate_confidence
from app.services.deal_analyzer import analyze_product
from app.services.product_repository import ProductRepository
from app.services.historical_comparison import HistoricalComparison


router = APIRouter(
    prefix="/scanner",
    tags=["Scanner"]
)


historical_comparison = HistoricalComparison()



@router.post("/barcode")
def scan_barcode(
    product_data: dict,
    db: Session = Depends(get_db)
):

    barcode = product_data["barcode"]
    buy_price = product_data["buy_price"]
    retailer = product_data["retailer"]


    lookup = lookup_barcode(barcode)


    if lookup is None:
        raise HTTPException(
            status_code=404,
            detail="Barcode not found"
        )


    repo = ProductRepository(db)


    #
    # CREATE OR UPDATE PRODUCT
    #

    product = repo.get_by_barcode(barcode)

    existing_product = product is not None


    if existing_product:

        product = repo.update_existing_product(
            product,
            buy_price
        )

        product.retailer = retailer

        db.commit()
        db.refresh(product)


    else:

        product = repo.create_product(
            lookup,
            buy_price,
            retailer
        )


    #
    # MARKET SNAPSHOT
    #

    market = MarketData(

        product_id=product.id,

        source="Barcode Lookup",

        marketplace="Internal Market Database",

        price=product.market_price,

        average_price=product.market_price,

        sold_count=25,

        condition="New"

    )


    db.add(market)

    db.commit()

    db.refresh(market)



    #
    # DEAL ANALYSIS
    #

    analysis = analyze_product(product)


    confidence = calculate_confidence(
        product,
        market
    )



    #
    # HISTORICAL COMPARISON
    #

    previous_history = (

        db.query(ScanHistory)

        .filter(
            ScanHistory.product_id == product.id
        )

        .all()

    )


    historical = historical_comparison.compare(

        current_buy_price=product.buy_price,

        current_roi=product.roi,

        history=previous_history

    )



    #
    # SAVE SCAN
    #

    scan = ScanHistory(

        product_id=product.id,

        recommendation=analysis["recommendation"],

        flipintel_score=analysis["flipintel_score"],

        confidence_score=confidence["confidence"],

        profit=product.profit,

        roi=product.roi

    )


    db.add(scan)

    db.commit()

    db.refresh(scan)



    return {

        "product_id": product.id,

        "existing_product": existing_product,

        "product": product.name,

        "brand": product.brand,

        "category": product.category,

        "market_price": product.market_price,

        "profit": product.profit,

        "roi": product.roi,

        "analysis": analysis,

        "confidence": confidence,

        "historical_comparison": historical,

        "scan_history_id": scan.id

    }