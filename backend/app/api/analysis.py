from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product
from app.models.deal_analysis import DealAnalysis
from app.models.market_data import MarketData

from app.services.deal_analyzer import analyze_product
from app.services.confidence_engine import calculate_confidence
from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine


router = APIRouter(
    prefix="/analysis",
    tags=["Analysis"]
)


flip_engine = FlipScoreEngine()

buy_engine = BuyPriceEngine()



#
# STANDARD PRODUCT ANALYSIS
#

@router.get("/{product_id}")
def analyze(
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


    analysis = analyze_product(product)



    saved_analysis = DealAnalysis(

        product_id=product.id,

        flipintel_score=
            analysis["flipintel_score"],

        recommendation=
            analysis["recommendation"],

        reasons=
            ", ".join(
                analysis["reasons"]
            )

    )


    db.add(saved_analysis)

    db.commit()

    db.refresh(saved_analysis)



    market = (
        db.query(MarketData)
        .filter(
            MarketData.product_id == product.id
        )
        .order_by(
            MarketData.checked_at.desc()
        )
        .first()
    )



    confidence = calculate_confidence(
        product,
        market
    )



    return {

        "product":
            product.name,


        "analysis":
            analysis,


        "confidence":
            confidence,


        "market_data":

            (

                {

                    "source":
                        market.source,

                    "marketplace":
                        market.marketplace,

                    "average_price":
                        market.average_price,

                    "sold_count":
                        market.sold_count,

                    "condition":
                        market.condition

                }

                if market else None

            ),


        "saved_analysis_id":
            saved_analysis.id

    }




#
# FLIP SCORE ENGINE
#

@router.get("/flip-score/{product_id}")
def flip_score(
    product_id: int,
    db: Session = Depends(get_db)
):

    result = flip_engine.calculate_score(

        product_id,

        db

    )


    return result




#
# BUY PRICE ENGINE
#

@router.get("/buy-price/{product_id}")
def buy_price(
    product_id: int,
    target_roi: float = 50,
    db: Session = Depends(get_db)
):

    result = buy_engine.calculate(

        product_id,

        db,

        target_roi

    )


    return result