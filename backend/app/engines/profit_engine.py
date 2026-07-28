class ProfitEngine:

    MAX_SCORE = 30

    def score(self, product):

        buy_price = float(product.buy_price or 0)

        market_price = float(
            product.market_price
            or product.sell_price
            or 0
        )

        estimated_profit = market_price - buy_price

        if estimated_profit >= 200:

            score = 30

        elif estimated_profit >= 100:

            score = 25

        elif estimated_profit >= 50:

            score = 15

        else:

            score = 5

        return {

            "name": "Profit",

            "score": score,

            "max_score": self.MAX_SCORE,

            "details": {

                "estimated_profit": round(
                    estimated_profit,
                    2
                )

            }

        }