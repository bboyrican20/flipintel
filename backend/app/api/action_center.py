from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory


router = APIRouter(
    prefix="/dashboard",
    tags=["Action Center"]
)


@router.get("/action-center")
def action_center(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()


    buy_now = []
    watch = []
    avoid = []


    for product in products:


        scan = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product.id
            )
            .order_by(
                ScanHistory.id.desc()
            )
            .first()
        )


        if not scan:
            continue



        deal = {

            "product_id": product.id,

            "product": product.name,

            "brand": product.brand,

            "profit": product.profit,

            "roi": product.roi,

            "confidence": scan.confidence_score,

            "score": (
                (product.profit or 0)
                +
                (product.roi or 0)
                +
                (scan.confidence_score or 0)
            )

        }



        if (
            scan.confidence_score >= 80
            and product.roi >= 50
        ):

            deal["action"] = "BUY"

            deal["reason"] = (
                "High confidence + strong resale spread"
            )

            buy_now.append(deal)



        elif (
            scan.confidence_score >= 50
        ):

            deal["action"] = "WATCH"

            deal["reason"] = (
                "Potential deal but needs monitoring"
            )

            watch.append(deal)



        else:

            deal["action"] = "AVOID"

            deal["reason"] = (
                "Low confidence or weak margins"
            )

            avoid.append(deal)



    buy_now.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    watch.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    avoid.sort(
        key=lambda x: x["score"],
        reverse=True
    )


    return {

        "buy_now": buy_now,

        "watch": watch,

        "avoid": avoid

    }