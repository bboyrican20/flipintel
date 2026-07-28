class DemandEngine:
    """
    Calculates the market demand score.
    Maximum Score: 10
    """

    MAX_SCORE = 10

    HIGH_DEMAND_CATEGORIES = {
        "power tools",
        "electronics",
        "gaming",
        "appliances",
        "lawn equipment",
    }

    def score(self, product):

        category = str(product.category or "").strip().lower()

        if category in self.HIGH_DEMAND_CATEGORIES:
            score = 10
            demand = "High"

        elif category:
            score = 6
            demand = "Medium"

        else:
            score = 3
            demand = "Unknown"

        return {
            "name": "Demand",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "category": product.category or "Unknown",
                "demand": demand
            }
        }