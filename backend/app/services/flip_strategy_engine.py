class FlipStrategyEngine:


    def generate_strategy(
        self,
        product
    ):


        buy_price = product.buy_price or 0


        market_price = (
            product.market_price
            or product.sell_price
            or 0
        )


        profit = (
            market_price - buy_price
        )


        roi = 0


        if buy_price > 0:

            roi = (
                profit / buy_price
            ) * 100



        listing_price = (
            market_price * 1.05
        )


        minimum_offer = (
            market_price * 0.90
        )



        if roi >= 100:

            strategy = (
                "Aggressive flip. "
                "List above market and allow negotiation."
            )


        elif roi >= 50:

            strategy = (
                "Strong opportunity. "
                "Price competitively for faster movement."
            )


        else:

            strategy = (
                "Lower margin flip. "
                "Focus on quick turnover."
            )



        return {


            "buy_price":
                round(
                    buy_price,
                    2
                ),


            "target_sale_price":
                round(
                    market_price,
                    2
                ),


            "recommended_listing":
                round(
                    listing_price,
                    2
                ),


            "minimum_offer":
                round(
                    minimum_offer,
                    2
                ),


            "expected_profit":
                round(
                    profit,
                    2
                ),


            "roi":
                round(
                    roi,
                    2
                ),


            "strategy":
                strategy

        }