class HistoricalComparison:


    def compare(
        self,
        current_buy_price: float,
        current_roi: float,
        history: list
    ):

        if not history:

            return {

                "status": "NO HISTORY",

                "message": "No previous scans available",

                "previous_best_buy": None,

                "average_buy_price": None,

                "improvement": None

            }


        previous_profits = []

        previous_rois = []



        for item in history:

            if item.profit is not None:

                previous_profits.append(
                    item.profit
                )


            if item.roi is not None:

                previous_rois.append(
                    item.roi
                )



        if previous_profits:

            best_previous_profit = max(
                previous_profits
            )

        else:

            best_previous_profit = 0



        if previous_rois:

            average_previous_roi = (
                sum(previous_rois)
                /
                len(previous_rois)
            )

        else:

            average_previous_roi = 0



        improvement = (

            current_roi
            -
            average_previous_roi

        )



        return {

            "status": "HISTORY_FOUND",

            "previous_best_profit": round(
                best_previous_profit,
                2
            ),

            "average_previous_roi": round(
                average_previous_roi,
                2
            ),

            "current_buy_price": current_buy_price,

            "current_roi": round(
                current_roi,
                2
            ),

            "roi_improvement": round(
                improvement,
                2
            ),

            "previous_scans": len(history)

        }



historical_comparison = HistoricalComparison()