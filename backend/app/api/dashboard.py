from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import get_db

from app.models.product import Product
from app.models.scan_history import ScanHistory
from app.services.ai_analysis_engine import AIAnalysisEngine


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)





@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):


    total_products = (
        db.query(Product)
        .count()
    )


    total_scans = (
        db.query(ScanHistory)
        .count()
    )


    strong_buys = (
        db.query(ScanHistory)
        .filter(
            ScanHistory.recommendation == "STRONG BUY"
        )
        .count()
    )


    average_roi = (
        db.query(
            func.avg(Product.roi)
        )
        .scalar()
    )


    total_profit = (
        db.query(
            func.sum(Product.profit)
        )
        .scalar()
    )


    invested_capital = (
        db.query(
            func.sum(Product.buy_price)
        )
        .scalar()
    )


    average_confidence = (
        db.query(
            func.avg(
                ScanHistory.confidence_score
            )
        )
        .scalar()
    )



    best_product = (
        db.query(Product)
        .order_by(
            Product.profit.desc()
        )
        .first()
    )



    dashboard_score = 0


    if strong_buys:
        dashboard_score += 25


    if average_roi and average_roi >= 100:
        dashboard_score += 25


    if total_profit and total_profit >= 500:
        dashboard_score += 25


    if average_confidence and average_confidence >= 80:
        dashboard_score += 25



    return {


        "dashboard_health_score":
            dashboard_score,


        "total_products":
            total_products,


        "total_scans":
            total_scans,


        "strong_buy_signals":
            strong_buys,


        "average_roi":
            round(
                average_roi or 0,
                2
            ),


        "total_profit_opportunity":
            round(
                total_profit or 0,
                2
            ),


        "capital_required":
            round(
                invested_capital or 0,
                2
            ),


        "average_confidence":
            round(
                average_confidence or 0,
                2
            ),



        "top_opportunity": {


            "product":
                best_product.name
                if best_product
                else None,


            "profit":
                best_product.profit
                if best_product
                else 0,


            "roi":
                best_product.roi
                if best_product
                else 0

        }

    }









@router.get("/top-deals")
def top_deals(
    db: Session = Depends(get_db)
):


    products = (

        db.query(Product)

        .order_by(
            Product.profit.desc()
        )

        .limit(5)

        .all()

    )



    deals = []



    for product in products:


        deals.append({

            "product_id":
                product.id,


            "product":
                product.name,


            "brand":
                product.brand,


            "category":
                product.category,


            "buy_price":
                product.buy_price,


            "market_price":
                product.market_price,


            "profit":
                product.profit,


            "roi":
                product.roi,


            "recommendation":

                "STRONG BUY"

                if product.roi >= 100

                else "WATCH",



            "flipintel_score":

                min(
                    100,
                    int(product.roi / 2)
                )

        })



    return {


        "total_deals":

            len(deals),


        "top_deals":

            deals

    }









@router.get("/brands")
def brand_intelligence(
    db: Session = Depends(get_db)
):


    results = (

        db.query(

            Product.brand,

            func.avg(Product.roi),

            func.count(Product.id)

        )

        .filter(

            Product.brand != None

        )

        .group_by(

            Product.brand

        )

        .order_by(

            func.avg(Product.roi).desc()

        )

        .all()

    )



    return {


        "top_brands": [


            {


                "brand":
                    brand,


                "average_roi":
                    round(
                        avg_roi or 0,
                        2
                    ),


                "products":
                    count


            }


            for brand, avg_roi, count in results


        ]

    }









@router.get("/categories")
def category_intelligence(
    db: Session = Depends(get_db)
):


    results = (

        db.query(

            Product.category,

            func.avg(Product.roi),

            func.count(Product.id)

        )

        .filter(

            Product.category != None

        )

        .group_by(

            Product.category

        )

        .order_by(

            func.avg(Product.roi).desc()

        )

        .all()

    )



    return {


        "categories": [


            {


                "category":
                    category,


                "average_roi":
                    round(
                        avg_roi or 0,
                        2
                    ),


                "products":
                    count


            }


            for category, avg_roi, count in results


        ]

    }


@router.get("/ai")
def dashboard_ai(
    db: Session = Depends(get_db)
):


    best_product = (
        db.query(Product)
        .order_by(
            Product.profit.desc()
        )
        .first()
    )


    if not best_product:

        return {
            "error": "No products available"
        }



    ai_engine = AIAnalysisEngine()



    return ai_engine.analyze(
        best_product.id,
        db
    )