from app.models.scan_history import ScanHistory


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

                average_roi = sum(valid_rois) / len(valid_rois)



        #
        # OPPORTUNITY SCORE
        #

        opportunity_score = flipintel_score


        reasons = []



        #
        # PROFIT BONUS
        #

        if profit >= 250:

            opportunity_score += 25

            reasons.append(
                "Exceptional profit potential"
            )


        elif profit >= 200:

            opportunity_score += 20

            reasons.append(
                "High profit potential"
            )



        #
        # ROI BONUS
        #

        if roi >= 150:

            opportunity_score += 25

            reasons.append(
                "Exceptional ROI"
            )


        elif roi >= 100:

            opportunity_score += 15

            reasons.append(
                "Excellent ROI"
            )



        #
        # HISTORY BONUS
        #

        if total_scans >= 10:

            opportunity_score += 15

            reasons.append(
                "Strong historical data"
            )


        elif total_scans >= 5:

            opportunity_score += 10

            reasons.append(
                "Historical validation"
            )



        #
        # MOMENTUM BONUS
        #

        if average_roi and roi > average_roi:

            improvement = roi - average_roi

            opportunity_score += 10

            reasons.append(
                f"ROI improving +{improvement:.2f}%"
            )



        return {


            "product_id": product.id,


            "product":
                product.name,


            "brand":
                product.brand,


            "retailer":
                product.retailer,


            "profit":
                product.profit,


            "roi":
                round(roi,2),


            "score":
                opportunity_score,


            "recommendation":
                analysis["recommendation"],


            "history_count":
                total_scans,


            "average_previous_roi":
                round(average_roi,2),


            "rank_reason":
                reasons

        }



opportunity_engine = OpportunityEngine()