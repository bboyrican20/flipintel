from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.product import Product
from app.services.deal_analyzer import analyze_product


router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)


@router.get("/")
def get_opportunities(
    db: Session = Depends(get_db)
):

    products = db.query(Product).all()

    opportunities = []


    for product in products:

        analysis = analyze_product(product)


        opportunities.append({

            "product_id": product.id,

            "product": product.name,

            "retailer": product.retailer,

            "score": analysis["flipintel_score"],

            "recommendation":
                analysis["recommendation"],

            "profit":
                product.profit,

            "roi":
                product.roi

        })


    opportunities.sort(
        key=lambda item: item["score"],
        reverse=True
    )


    return {
        "total_opportunities": len(opportunities),
        "opportunities": opportunities
    }