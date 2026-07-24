from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory
from app.models.market_data import MarketData

from app.services.product_memory import ProductMemory


router = APIRouter(
    prefix="/products",
    tags=["Product History"]
)


memory = ProductMemory()



@router.get("/{product_id}/history")
def product_history(
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



    scans = (

        db.query(ScanHistory)

        .filter(
            ScanHistory.product_id == product_id
        )

        .all()

    )



    market = (

        db.query(MarketData)

        .filter(
            MarketData.product_id == product_id
        )

        .all()

    )



    insights = memory.analyze(

        product,

        scans,

        market

    )



    return {


        "product_id": product.id,


        "product": product.name,


        "brand": product.brand,


        "insights": insights,


        "scan_count": len(scans)


    }