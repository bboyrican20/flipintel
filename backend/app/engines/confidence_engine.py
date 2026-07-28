class ConfidenceEngine:

    MAX_SCORE = 10

    def score(self, product, history_result):

        confidence = 5

        buy_price = float(product.buy_price or 0)

        market_price = float(
            product.market_price
            or product.sell_price
            or 0
        )

        scan_count = history_result["details"]["scan_count"]

        if buy_price > 0:

            roi = (
                (market_price - buy_price)
                / buy_price
            ) * 100

        else:

            roi = 0

        if roi >= 100:

            confidence += 2

        if scan_count >= 10:

            confidence += 2

        elif scan_count >= 5:

            confidence += 1

        confidence = min(
            confidence,
            self.MAX_SCORE
        )

        return {

            "name": "Confidence",

            "score": confidence,

            "max_score": self.MAX_SCORE,

            "details": {

                "confidence_percent":
                    confidence * 10

            }

        }