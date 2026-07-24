from app.models.product import Product
from app.models.market_data import MarketData


def calculate_confidence(
    product: Product,
    market: MarketData | None
):

    confidence = 50

    reasons = []


    # ROI

    if (product.roi or 0) >= 100:
        confidence += 15
        reasons.append("Excellent ROI")

    elif (product.roi or 0) >= 50:
        confidence += 10
        reasons.append("Strong ROI")


    # Profit

    if (product.profit or 0) >= 100:
        confidence += 15
        reasons.append("High profit")

    elif (product.profit or 0) >= 50:
        confidence += 10
        reasons.append("Good profit")


    # Brand

    if product.brand:
        confidence += 10
        reasons.append(f"Trusted brand: {product.brand}")


    # Market Data

    if market:

        if market.sold_count and market.sold_count >= 25:
            confidence += 20
            reasons.append("High market demand")

        if (
            market.average_price
            and product.buy_price
            and market.average_price >
            product.buy_price * 1.5
        ):
            confidence += 15
            reasons.append("Excellent resale spread")


    confidence = min(confidence, 100)


    if confidence >= 90:
        risk = "LOW"

    elif confidence >= 70:
        risk = "MEDIUM"

    else:
        risk = "HIGH"


    return {

        "confidence": confidence,

        "risk": risk,

        "reasons": reasons

    }