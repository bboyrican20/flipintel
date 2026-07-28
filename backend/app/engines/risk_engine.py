class RiskEngine:
    """
    Calculates the product risk score.
    Maximum Score: 10
    """

    MAX_SCORE = 10

    def score(self, history_result):

        scan_count = (
            history_result["details"]["scan_count"]
        )

        if scan_count >= 10:
            score = 10
            risk = "Low"

        elif scan_count >= 5:
            score = 8
            risk = "Moderate"

        elif scan_count > 0:
            score = 6
            risk = "Elevated"

        else:
            score = 5
            risk = "Unknown"

        return {
            "name": "Risk",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "risk_level": risk
            }
        }