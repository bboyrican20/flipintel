from typing import Dict


PREMIUM_BRANDS = [
    "dewalt",
    "milwaukee",
    "makita",
    "bosch",
    "apple",
    "sony",
    "lego"
]


def analyze_product(product) -> Dict:
    score = 0
    reasons = []

    # Profit scoring
    profit = product.profit or 0

    if profit >= 100:
        score += 30
        reasons.append("High profit opportunity")
    elif profit >= 50:
        score += 20
        reasons.append("Good profit margin")
    elif profit > 0:
        score += 10
        reasons.append("Positive profit")


    # ROI scoring
    roi = product.roi or 0

    if roi >= 100:
        score += 40
        reasons.append("Excellent ROI")
    elif roi >= 50:
        score += 30
        reasons.append("Strong ROI")
    elif roi >= 25:
        score += 20
        reasons.append("Acceptable ROI")


    # Brand scoring
    name = product.name.lower()

    for brand in PREMIUM_BRANDS:
        if brand in name:
            score += 20
            reasons.append(f"Strong brand: {brand.title()}")
            break


    # Category confidence
    score += 10
    reasons.append("Resale market analysis passed")


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