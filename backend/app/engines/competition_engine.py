class CompetitionEngine:
    """
    Calculates the competition score.
    Maximum Score: 10
    """

    MAX_SCORE = 10

    def score(self, product):

        competition = getattr(product, "competition_level", None)

        if competition is None:
            score = 6
            level = "Unknown"

        else:
            value = str(competition).strip().lower()

            if value == "low":
                score = 10
                level = "Low"

            elif value == "medium":
                score = 7
                level = "Medium"

            elif value == "high":
                score = 4
                level = "High"

            else:
                score = 6
                level = "Unknown"

        return {
            "name": "Competition",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "competition_level": level
            }
        }