from app.models.product import Product
from app.models.scan_history import ScanHistory
from sqlalchemy.orm import Session


def calculate_deal_rank(product, scan=None):

    score = 0


    # FlipIntel analysis score
    if scan:
        score += scan.flipintel_score


    # Confidence score
    if scan:
        score += scan.confidence_score


    # ROI weighting
    if product.roi:

        if product.roi >= 100:
            score += 30

        elif product.roi >= 75:
            score += 20

        elif product.roi >= 50:
            score += 10



    # Profit weighting

    if product.profit:

        if product.profit >= 200:
            score += 20

        elif product.profit >= 100:
            score += 10



    return score



def get_top_deals(db: Session, limit=10):


    products = (
        db.query(Product)
        .all()
    )


    ranked = []


    for product in products:


        scan = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product.id
            )
            .order_by(
                ScanHistory.scanned_at.desc()
            )
            .first()
        )


        deal_score = calculate_deal_rank(
            product,
            scan
        )


        ranked.append({

            "product_id":
                product.id,

            "product":
                product.name,

            "brand":
                product.brand,

            "profit":
                product.profit,

            "roi":
                product.roi,

            "flipintel_score":
                scan.flipintel_score if scan else None,

            "confidence":
                scan.confidence_score if scan else None,

            "deal_score":
                deal_score,

            "recommendation":
                scan.recommendation if scan else "UNANALYZED"

        })



    ranked.sort(
        key=lambda x: x["deal_score"],
        reverse=True
    )


    for index, deal in enumerate(ranked, start=1):

        deal["rank"] = index



    return ranked[:limit]