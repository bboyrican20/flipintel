class OpportunityEngine:


    def rank_product(
        self,
        product,
        analysis,
        history
    ):


        flipintel_score = analysis["flipintel_score"]


        total_scans = len(history)


        profit = product.profit or 0

        roi = product.roi or 0


        average_roi = 0


        if history:

            valid_rois = [
                scan.roi
                for scan in history
                if scan.roi is not None
            ]

            if valid_rois:

                average_roi = (
                    sum(valid_rois)
                    /
                    len(valid_rois)
                )



        #
        # OPPORTUNITY SCORE
        #

        opportunity_score = flipintel_score


        reasons = []


        #
        # PROFIT INTELLIGENCE
        #

        if profit >= 250:

            opportunity_score += 30

            reasons.append(
                "Exceptional profit opportunity"
            )


        elif profit >= 200:

            opportunity_score += 20

            reasons.append(
                "High profit opportunity"
            )


        elif profit >= 100:

            opportunity_score += 10

            reasons.append(
                "Positive profit margin"
            )



        #
        # ROI INTELLIGENCE
        #

        if roi >= 150:

            opportunity_score += 30

            reasons.append(
                "Exceptional ROI"
            )


        elif roi >= 100:

            opportunity_score += 20

            reasons.append(
                "Excellent ROI"
            )


        elif roi >= 50:

            opportunity_score += 10

            reasons.append(
                "Acceptable ROI"
            )



        #
        # HISTORY INTELLIGENCE
        #

        if total_scans >= 10:

            opportunity_score += 20

            reasons.append(
                "Strong historical validation"
            )


        elif total_scans >= 5:

            opportunity_score += 10

            reasons.append(
                "Product has scan history"
            )



        #
        # PERFORMANCE MOMENTUM
        #

        improvement = 0


        if average_roi and roi > average_roi:

            improvement = roi - average_roi

            opportunity_score += 15

            reasons.append(
                f"ROI improving +{improvement:.2f}%"
            )



        #
        # ACTION RECOMMENDATION
        #

        if opportunity_score >= 150:

            action = "BUY NOW"


        elif opportunity_score >= 100:

            action = "CONSIDER"


        else:

            action = "PASS"



        #
        # PRICE INTELLIGENCE
        #

        price_signal = None


        if product.market_price:

            recommended_buy = (
                product.market_price / 1.75
            )


            if product.buy_price <= recommended_buy:

                opportunity_score += 10

                price_signal = (
                    "Buying below recommended acquisition price"
                )

                reasons.append(
                    price_signal
                )



        #
        # FINAL OUTPUT
        #

        return {


            "product_id":
                product.id,


            "product":
                product.name,


            "brand":
                product.brand,


            "retailer":
                product.retailer,


            "profit":
                product.profit,


            "roi":
                round(
                    roi,
                    2
                ),


            "score":
                opportunity_score,


            "action":
                action,


            "recommendation":
                analysis["recommendation"],


            "history_count":
                total_scans,


            "average_previous_roi":
                round(
                    average_roi,
                    2
                ),


            "rank_reason":
                reasons

        }



opportunity_engine = OpportunityEngine()