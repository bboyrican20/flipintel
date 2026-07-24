from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.scan_history import ScanHistory
from app.models.product import Product


router = APIRouter(
    prefix="/history",
    tags=["History"]
)


@router.get("/product/{product_id}")
def product_history(
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


    scans = (
        db.query(ScanHistory)
        .filter(
            ScanHistory.product_id == product_id
        )
        .order_by(
            ScanHistory.scanned_at.desc()
        )
        .all()
    )


    if not scans:
        return {
            "product": product.name,
            "total_scans": 0,
            "message": "No scan history available"
        }


    best_profit = max(
        scan.profit for scan in scans
    )


    best_roi = max(
        scan.roi for scan in scans
    )


    average_roi = (
        sum(scan.roi for scan in scans)
        /
        len(scans)
    )


    return {

        "product": product.name,

        "brand": product.brand,

        "category": product.category,


        "total_scans": len(scans),


        "best_purchase": {

            "profit": best_profit,

            "roi": best_roi

        },


        "average_roi": round(
            average_roi,
            2
        ),


        "latest_scan": {

            "buy_price": product.buy_price,

            "profit": product.profit,

            "roi": product.roi

        },


        "scan_history": [

            {

                "id": scan.id,

                "recommendation": scan.recommendation,

                "score": scan.flipintel_score,

                "confidence": scan.confidence_score,

                "profit": scan.profit,

                "roi": scan.roi,

                "date": scan.scanned_at

            }

            for scan in scans

        ]

    }