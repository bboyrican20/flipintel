class ROIEngine:

    MAX_SCORE = 25

    def score(self, product):

        buy_price = float(product.buy_price or 0)

        market_price = float(
            product.market_price
            or product.sell_price
            or 0
        )

        if buy_price > 0:

            roi = (
                (market_price - buy_price)
                / buy_price
            ) * 100

        else:

            roi = 0

        if roi >= 150:

            score = 25

        elif roi >= 75:

            score = 20

        elif roi >= 30:

            score = 12

        else:

            score = 5

        return {

            "name": "ROI",

            "score": score,

            "max_score": self.MAX_SCORE,

            "details": {

                "estimated_roi": round(
                    roi,
                    2
                )

            }

        }