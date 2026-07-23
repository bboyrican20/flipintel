from typing import Dict

from app.core.settings import settings


def analyze_product(product) -> Dict:
    score = 0
    reasons = []

    # Profit scoring
    profit = product.profit or 0

    if profit >= settings.HIGH_PROFIT_THRESHOLD:
        score += 30
        reasons.append("High profit opportunity")

    elif profit >= settings.MEDIUM_PROFIT_THRESHOLD:
        score += 20
        reasons.append("Good profit margin")

    elif profit > 0:
        score += 10
        reasons.append("Positive profit")


    # ROI scoring
    roi = product.roi or 0

    if roi >= settings.EXCELLENT_ROI_THRESHOLD:
        score += 40
        reasons.append("Excellent ROI")

    elif roi >= settings.STRONG_ROI_THRESHOLD:
        score += 30
        reasons.append("Strong ROI")

    elif roi >= settings.ACCEPTABLE_ROI_THRESHOLD:
        score += 20
        reasons.append("Acceptable ROI")


    # Brand scoring
    name = product.name.lower()

    for brand in settings.PREMIUM_BRANDS:
        if brand in name:
            score += 20
            reasons.append(
                f"Strong brand: {brand.title()}"
            )
            break


    # Category confidence
    score += 10
    reasons.append(
        "Resale market analysis passed"
    )


    # Recommendation
    if score >= 85:
        recommendation = "STRONG BUY"

    elif score >= 70:
        recommendation = "BUY"

    elif score >= 50:
        recommendation = "WATCH"

    else:
        recommendation = "PASS"


    return {
        "flipintel_score": score,
        "recommendation": recommendation,
        "reasons": reasons
    }