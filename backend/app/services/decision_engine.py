class DecisionEngine:


    def evaluate(
        self,
        product,
        analysis,
        confidence,
        historical
    ):


        roi = product.roi or 0
        profit = product.profit or 0
        market_price = product.market_price or 0


        reasons = []
        warnings = []


        #
        # MAX BUY PRICE
        #
        # Target 75% ROI minimum
        #

        max_buy_price = round(
            market_price / 1.75,
            2
        )



        #
        # DEAL GRADE
        #

        score = 0


        if roi >= 150:
            score += 40
            reasons.append(
                "Exceptional ROI"
            )

        elif roi >= 100:
            score += 30
            reasons.append(
                "Excellent ROI"
            )

        elif roi >= 50:
            score += 20



        if profit >= 250:
            score += 30
            reasons.append(
                "Exceptional profit potential"
            )

        elif profit >= 150:
            score += 20
            reasons.append(
                "Strong profit potential"
            )



        if confidence.get("confidence",0) >= 90:
            score += 20
            reasons.append(
                "High confidence prediction"
            )



        if historical:

            if historical.get(
                "roi_improvement",
                0
            ) > 0:

                score += 10

                reasons.append(
                    "Historical performance improving"
                )



        #
        # ACTION
        #

        if score >= 85:

            action = "BUY"
            grade = "S-TIER"


        elif score >= 65:

            action = "BUY"
            grade = "A-TIER"


        elif score >= 45:

            action = "CONSIDER"
            grade = "B-TIER"


        else:

            action = "PASS"
            grade = "C-TIER"



        #
        # WARNINGS
        #

        if product.buy_price > max_buy_price:

            warnings.append(
                "Current buy price exceeds recommended acquisition price"
            )



        if roi < 50:

            warnings.append(
                "Low ROI margin"
            )



        return {


            "action":
                action,


            "grade":
                grade,


            "max_buy_price":
                max_buy_price,


            "current_buy_price":
                product.buy_price,


            "risk":
                "LOW"
                if confidence.get("confidence",0) >= 80
                else "MEDIUM",


            "reasons":
                reasons,


            "warnings":
                warnings

        }



decision_engine = DecisionEngine()