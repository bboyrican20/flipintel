from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory

from app.services.deal_analyzer import analyze_product
from app.services.opportunity_engine import opportunity_engine


router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)


@router.get("/")
def get_opportunities(
    db: Session = Depends(get_db)
):


    products = (
        db.query(Product)
        .all()
    )


    opportunities = []



    for product in products:


        analysis = analyze_product(product)



        history = (

            db.query(ScanHistory)

            .filter(
                ScanHistory.product_id == product.id
            )

            .all()

        )



        ranked = opportunity_engine.rank_product(

            product,

            analysis,

            history

        )


        opportunities.append(ranked)




    opportunities.sort(

        key=lambda item:
            item["score"],

        reverse=True

    )



    return {


        "total_opportunities":

            len(opportunities),



        "top_opportunity":

            opportunities[0]
            if opportunities
            else None,



        "opportunities":

            opportunities

    }