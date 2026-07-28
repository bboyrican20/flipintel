class CategoryEngine:
    """
    Calculates the category quality score.
    Maximum Score: 10
    """

    MAX_SCORE = 10

    CATEGORY_SCORES = {
        "power tools": 10,
        "electronics": 10,
        "gaming": 9,
        "appliances": 8,
        "lawn equipment": 8,
        "automotive": 7,
        "home improvement": 7,
        "hand tools": 6,
    }

    def score(self, product):

        category = str(getattr(product, "category", "") or "").strip().lower()

        score = self.CATEGORY_SCORES.get(category, 5)

        return {
            "name": "Category",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "category": category.title() if category else "Unknown"
            }
        }