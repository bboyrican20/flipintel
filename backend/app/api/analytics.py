from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.analytics_engine import AnalyticsEngine
from app.services.retailer_engine import RetailerEngine


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


engine = AnalyticsEngine()

retailer_engine = RetailerEngine()



@router.get("/dashboard")
def dashboard(
    db: Session = Depends(get_db)
):

    portfolio = (
        engine.portfolio_summary(db)
    )


    best_flip = (
        engine.best_flip(db)
    )


    performance = (
        engine.performance_summary(db)
    )


    brands = (
        engine.brand_performance(db)
    )


    retailers = (
        retailer_engine.retailer_performance(db)
    )


    return {

        "portfolio":
            {

                "total_items":
                    portfolio["total_items"],

                "sold_flips":
                    portfolio["sold_flips"],

                "active_inventory":
                    portfolio["active_inventory"]

            },


        "financials":
            {

                "capital_invested":
                    portfolio["capital_invested"],

                "revenue_generated":
                    portfolio["revenue_generated"],

                "realized_profit":
                    portfolio["realized_profit"],

                "projected_profit":
                    portfolio["projected_profit"],

                "roi":
                    portfolio["roi"]

            },


        "best_flip":
            best_flip,


        "performance":
            performance,


        "top_brands":
            brands,


        "retailers":
            retailers

    }