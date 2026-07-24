from statistics import mean


class ProductMemory:


    def analyze(
        self,
        product,
        scans,
        market_data
    ):


        if not scans:

            return {

                "times_scanned": 0,

                "average_buy_price": product.buy_price,

                "best_buy_price": product.buy_price,

                "average_roi": 0,

                "historical_performance": "NO DATA"

            }



        buy_prices = []

        roi_values = []



        for scan in scans:


            if scan.profit is not None:

                buy_price = product.market_price - scan.profit

                buy_prices.append(
                    buy_price
                )


            if scan.roi is not None:

                roi_values.append(
                    scan.roi
                )



        average_buy = round(
            mean(buy_prices),
            2
        ) if buy_prices else product.buy_price



        best_buy = min(
            buy_prices
        ) if buy_prices else product.buy_price



        average_roi = round(
            mean(roi_values),
            2
        ) if roi_values else 0



        if average_roi >= 75:

            performance = "EXCELLENT"



        elif average_roi >= 40:

            performance = "GOOD"



        else:

            performance = "WEAK"



        return {


            "times_scanned": len(scans),


            "average_buy_price": average_buy,


            "best_buy_price": best_buy,


            "average_roi": average_roi,


            "historical_performance": performance

        }