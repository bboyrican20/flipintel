from statistics import mean


class MarketIntelligence:


    def __init__(self):
        pass



    def analyze_market(
        self,
        product_name: str,
        market_data: list
    ):

        if not market_data:

            return {

                "market_value": 0,

                "average_price": 0,

                "sold_volume": 0,

                "demand_score": 0,

                "market_confidence": 0

            }



        prices = []

        sold_volume = 0


        for item in market_data:

            if item.get("price"):

                prices.append(
                    item["price"]
                )


            if item.get("sold_count"):

                sold_volume += item["sold_count"]



        average_price = round(
            mean(prices),
            2
        ) if prices else 0



        demand_score = self.calculate_demand(
            sold_volume
        )


        confidence = self.calculate_confidence(
            len(prices),
            sold_volume
        )



        return {

            "product": product_name,

            "market_value": average_price,

            "average_price": average_price,

            "sold_volume": sold_volume,

            "demand_score": demand_score,

            "market_confidence": confidence

        }



    def calculate_demand(
        self,
        sold_volume: int
    ):

        if sold_volume >= 100:

            return 100


        if sold_volume >= 50:

            return 90


        if sold_volume >= 25:

            return 75


        if sold_volume >= 10:

            return 50


        return 25




    def calculate_confidence(
        self,
        sources: int,
        sold_volume: int
    ):

        score = 0


        if sources >= 3:

            score += 40

        elif sources >= 1:

            score += 25



        if sold_volume >= 50:

            score += 40

        elif sold_volume >= 25:

            score += 30

        elif sold_volume >= 10:

            score += 20



        if score > 100:

            score = 100


        return score