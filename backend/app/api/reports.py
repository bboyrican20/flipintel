from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.product import Product
from app.services.deal_analyzer import analyze_product


router = APIRouter(
    prefix="/analysis",
    tags=["Reports"]
)


@router.get("/report/{product_id}")
def deal_report(
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


    score = analysis["flipintel_score"]


    if score >= 85:
        confidence = "VERY HIGH"

    elif score >= 70:
        confidence = "HIGH"

    elif score >= 50:
        confidence = "MEDIUM"

    else:
        confidence = "LOW"


    risks = []


    if product.profit < 100:
        risks.append(
            "Profit opportunity below $100"
        )


    if product.roi < 50:
        risks.append(
            "ROI below preferred threshold"
        )


    return {

        "product": product.name,


        "flipintel": {
            "score": score,
            "decision": analysis["recommendation"],
            "confidence": confidence
        },


        "financials": {

            "buy_price": product.buy_price,

            "expected_sale": product.sell_price,

            "profit": product.profit,

            "roi": product.roi

        },


        "strengths": analysis["reasons"],


        "risks": risks,


        "summary":
            f"{product.name} received a "
            f"{analysis['recommendation']} recommendation "
            f"with a FlipIntel score of "
            f"{score}/100."

    }