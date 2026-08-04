from statistics import mean


class MarketplaceEngine:

    def analyze(self, lookup: dict):

        market_price = float(
            lookup.get("market_price", 0)
        )

        #
        # Temporary mock marketplace prices
        # (Later these become live API calls.)
        #

        ebay_price = round(
            market_price * 1.03,
            2
        )

        amazon_price = round(
            market_price * 1.08,
            2
        )

        facebook_price = round(
            market_price * 0.96,
            2
        )

        average_price = round(

            mean(
                [

                    ebay_price,

                    amazon_price,

                    facebook_price

                ]

            ),

            2

        )

        highest = max(

            ebay_price,

            amazon_price,

            facebook_price

        )

        lowest = min(

            ebay_price,

            amazon_price,

            facebook_price

        )

        return {

            "market_price": average_price,

            "sources": {

                "ebay": ebay_price,

                "amazon": amazon_price,

                "facebook": facebook_price

            },

            "highest": highest,

            "lowest": lowest,

            "spread": round(
                highest - lowest,
                2
            ),

            "confidence": 92

        }