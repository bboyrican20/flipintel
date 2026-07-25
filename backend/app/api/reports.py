from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory

from app.services.deal_analyzer import analyze_product
from app.services.confidence_engine import calculate_confidence
from app.services.decision_engine import DecisionEngine
from app.services.opportunity_engine import opportunity_engine



router = APIRouter(
    prefix="/analysis",
    tags=["Reports"]
)


decision_engine = DecisionEngine()



@router.get("/report/{product_id}")
def deal_report(
    product_id: int,
    db: Session = Depends(get_db)
):


    product = (

        db.query(Product)

        .filter(
            Product.id == product_id
        )

        .first()

    )


    if not product:

        raise HTTPException(

            status_code=404,

            detail="Product not found"

        )



    analysis = analyze_product(product)



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



    confidence = {

        "confidence":
            latest_scan.confidence_score
            if latest_scan
            else 0

    }



    decision = decision_engine.decide(

        product,

        analysis,

        confidence,

        {}

    )



    opportunity = opportunity_engine.rank_product(

        product,

        analysis,

        history

    )



    inventory_plan = {

        "recommended_units": 1,

        "capital_required": product.buy_price,

        "projected_revenue":
            round(
                product.market_price,
                2
            ),

        "projected_profit":
            round(
                product.profit,
                2
            )

    }



    risks = []



    if product.roi < 50:

        risks.append(
            "ROI below preferred threshold"
        )


    if product.profit < 100:

        risks.append(
            "Low profit opportunity"
        )


    if decision["warnings"]:

        risks.extend(
            decision["warnings"]
        )



    return {


        "product": product.name,


        "brand": product.brand,


        "retailer": product.retailer,



        "decision": {


            "action":
                decision["action"],


            "grade":
                decision["grade"],


            "risk":
                decision["risk"],


            "max_buy_price":
                decision["max_buy_price"]

        },



        "financials": {


            "current_buy_price":
                product.buy_price,


            "market_value":
                product.market_price,


            "profit":
                product.profit,


            "roi":
                round(
                    product.roi,
                    2
                )

        },



        "inventory_projection":

            inventory_plan,



        "opportunity_score":

            opportunity["score"],



        "history": {


            "times_scanned":
                len(history),


            "average_roi":

                round(

                    sum(
                        x.roi
                        for x in history
                        if x.roi
                    )
                    /
                    len(history),

                    2

                )
                if history
                else 0

        },



        "why_buy":

            opportunity["rank_reason"],



        "risks":

            risks,



        "summary":

            (
                f"{product.name} is rated "
                f"{decision['grade']} with a "
                f"{decision['action']} recommendation. "
                f"Current ROI is "
                f"{product.roi:.2f}% with "
                f"${product.profit:.2f} profit potential."
            )

    }