class BrandEngine:
    """
    Calculates the brand score for a product.
    Maximum Score: 20
    """

    MAX_SCORE = 20

    PREMIUM_BRANDS = {
        "milwaukee",
        "dewalt",
        "makita",
        "bosch",
        "festool"
    }

    def score(self, product):
        brand = str(product.brand or "").strip().lower()

        if brand in self.PREMIUM_BRANDS:
            score = 20
            tier = "Premium"

        elif brand:
            score = 10
            tier = "Standard"

        else:
            score = 5
            tier = "Unknown"

        return {
            "name": "Brand",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "brand": product.brand or "Unknown",
                "tier": tier
            }
        }