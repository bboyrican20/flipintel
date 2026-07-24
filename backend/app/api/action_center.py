from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory
from app.models.market_data import MarketData

from app.services.market_intelligence import MarketIntelligence
from app.services.deal_intelligence import DealIntelligence
from app.services.deal_explainer import DealExplainer


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


market_engine = MarketIntelligence()

deal_engine = DealIntelligence()

explainer = DealExplainer()



@router.get("/action-center")
def action_center(
    db: Session = Depends(get_db)
):

    products = (
        db.query(Product)
        .all()
    )


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



        market_rows = (
            db.query(MarketData)
            .filter(
                MarketData.product_id == product.id
            )
            .all()
        )



        market_data = []


        for row in market_rows:

            market_data.append({

                "price": row.price,

                "sold_count": row.sold_count

            })



        intelligence = market_engine.analyze_market(

            product.name,

            market_data

        )



        deal_score = deal_engine.calculate_score(

            product.profit,

            product.roi,

            scan.confidence_score,

            intelligence["demand_score"],

            intelligence["market_confidence"]

        )



        recommendation = deal_engine.recommendation(

            deal_score

        )



        explanation = explainer.explain(

            product,

            product.profit,

            product.roi,

            intelligence["demand_score"],

            intelligence["market_confidence"],

            recommendation

        )



        deal = {


            "product_id": product.id,


            "product": product.name,


            "brand": product.brand,


            "profit": product.profit,


            "roi": product.roi,


            "confidence": scan.confidence_score,


            "market_demand": intelligence["demand_score"],


            "market_confidence": intelligence["market_confidence"],


            "market_value": intelligence["market_value"],


            "deal_score": deal_score,


            "action": recommendation,


            "explanation": explanation["explanation"],


            "signals": explanation["signals"]

        }



        if recommendation in [

            "STRONG BUY",

            "BUY"

        ]:

            buy_now.append(deal)



        elif recommendation == "WATCH":

            watch.append(deal)



        else:

            avoid.append(deal)



    buy_now.sort(

        key=lambda x: x["deal_score"],

        reverse=True

    )


    watch.sort(

        key=lambda x: x["deal_score"],

        reverse=True

    )


    avoid.sort(

        key=lambda x: x["deal_score"],

        reverse=True

    )



    return {


        "buy_now": buy_now,


        "watch": watch,


        "avoid": avoid

    }