class MarketplaceEngine:


    def analyze(
        self,
        product
    ):


        roi = product.roi or 0
        profit = product.profit or 0
        buy_price = product.buy_price or 0



        #
        # Determine expected sale price
        #

        if product.market_price:

            expected_sale = product.market_price

        else:

            expected_sale = buy_price + profit





        if roi >= 100 and profit >= 50:

            best_marketplace = "Facebook Marketplace"

            sell_speed = "FAST"

            confidence = 92


        elif roi >= 50:

            best_marketplace = "eBay"

            sell_speed = "MEDIUM"

            confidence = 82


        else:

            best_marketplace = "OfferUp"

            sell_speed = "SLOW"

            confidence = 65





        alternatives = [

            {

                "marketplace": "Facebook Marketplace",

                "expected_price": round(
                    expected_sale,
                    2
                ),

                "sell_speed": "FAST"

            },


            {

                "marketplace": "eBay",

                "expected_price": round(
                    expected_sale * 0.97,
                    2
                ),

                "sell_speed": "MEDIUM"

            },


            {

                "marketplace": "OfferUp",

                "expected_price": round(
                    expected_sale * 0.90,
                    2
                ),

                "sell_speed": "FAST"

            }

        ]





        return {


            "best_marketplace":

                best_marketplace,


            "expected_sale_price":

                round(
                    expected_sale,
                    2
                ),


            "sell_speed":

                sell_speed,


            "confidence":

                confidence,


            "alternatives":

                alternatives

        }