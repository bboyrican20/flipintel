class ProductMemory:

    def summarize(
        self,
        product,
        history
    ):

        if not history:

            return {
                "status": "NEW_PRODUCT",
                "times_seen": 0,
                "best_buy_price": None,
                "average_buy_price": None,
                "highest_roi": 0,
                "average_roi": 0,
                "buy_zone": None,
                "message": "First time this product has been scanned."
            }

        total = len(history)

        rois = [
            scan.roi
            for scan in history
            if scan.roi is not None
        ]

        average_roi = (
            sum(rois) / len(rois)
            if rois else 0
        )

        highest_roi = (
            max(rois)
            if rois else 0
        )

        best_buy_price = product.market_price - highest_roi if product.market_price else product.buy_price

        average_buy_price = (
            product.market_price - average_roi
            if product.market_price else product.buy_price
        )

        if average_roi >= 100:
            buy_zone = "AGGRESSIVE BUY"

        elif average_roi >= 70:
            buy_zone = "BUY"

        elif average_roi >= 40:
            buy_zone = "WATCH"

        else:
            buy_zone = "PASS"

        return {

            "status": "KNOWN_PRODUCT",

            "times_seen": total,

            "best_buy_price": round(best_buy_price, 2),

            "average_buy_price": round(average_buy_price, 2),

            "highest_roi": round(highest_roi, 2),

            "average_roi": round(average_roi, 2),

            "buy_zone": buy_zone,

            "message": (
                f"Scanned {total} times. "
                f"Average ROI {average_roi:.1f}%. "
                f"Best ROI {highest_roi:.1f}%."
            )

        }


product_memory = ProductMemory()