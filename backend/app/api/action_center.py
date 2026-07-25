from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory
from app.models.market_data import MarketData

from app.services.market_intelligence import MarketIntelligence
from app.services.deal_intelligence import DealIntelligence
from app.services.deal_explainer import DealExplainer
from app.services.decision_engine import DecisionEngine
from app.services.opportunity_engine import opportunity_engine
from app.services.deal_analyzer import analyze_product



router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


market_engine = MarketIntelligence()

deal_engine = DealIntelligence()

explainer = DealExplainer()

decision_engine = DecisionEngine()



@router.get("/action-center")
def action_center(
    db: Session = Depends(get_db)
):


    products = (
        db.query(Product)
        .all()
    )


    actions = []



    for product in products:


        history = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product.id
            )
            .all()
        )


        latest_scan = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product.id
            )
            .order_by(
                ScanHistory.id.desc()
            )
            .first()
        )


        if not latest_scan:
            continue



        analysis = analyze_product(product)



        market_rows = (
            db.query(MarketData)
            .filter(
                MarketData.product_id == product.id
            )
            .all()
        )


        market_data = [

            {
                "price": row.price,
                "sold_count": row.sold_count
            }

            for row in market_rows

        ]



        intelligence = market_engine.analyze_market(

            product.name,

            market_data

        )



        deal_score = deal_engine.calculate_score(

            product.profit,

            product.roi,

            latest_scan.confidence_score,

            intelligence["demand_score"],

            intelligence["market_confidence"]

        )



        recommendation = deal_engine.recommendation(

            deal_score

        )



        decision = decision_engine.decide(

            product,

            analysis,

            {
                "confidence":
                    latest_scan.confidence_score
            },

            {}

        )



        ranked = opportunity_engine.rank_product(

            product,

            analysis,

            history

        )



        explanation = explainer.explain(

            product,

            product.profit,

            product.roi,

            intelligence["demand_score"],

            intelligence["market_confidence"],

            recommendation

        )



        actions.append({


            "product_id":
                product.id,


            "product":
                product.name,


            "brand":
                product.brand,


            "retailer":
                product.retailer,


            "priority":
                ranked["action"],


            "score":
                ranked["score"],


            "deal_score":
                deal_score,


            "profit":
                product.profit,


            "roi":
                round(product.roi,2),


            "max_buy_price":
                decision["max_buy_price"],


            "current_buy_price":
                product.buy_price,


            "expected_return":
                product.profit,


            "confidence":
                latest_scan.confidence_score,


            "reasons":
                ranked["rank_reason"],


            "explanation":
                explanation["explanation"]


        })



    actions.sort(

        key=lambda x:
            x["score"],

        reverse=True

    )



    return {


        "total_actions":
            len(actions),


        "top_action":
            actions[0]
            if actions
            else None,


        "actions":
            actions

    }