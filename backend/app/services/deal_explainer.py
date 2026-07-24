class DealExplainer:


    def explain(
        self,
        product,
        profit,
        roi,
        demand,
        confidence,
        action,
        historical=None
    ):


        signals = []


        #
        # ROI Intelligence
        #

        if roi >= 100:

            signals.append(
                "Excellent ROI opportunity"
            )

        elif roi >= 50:

            signals.append(
                "Strong ROI opportunity"
            )

        else:

            signals.append(
                "Low ROI opportunity"
            )



        #
        # Profit Intelligence
        #

        if profit >= 200:

            signals.append(
                "High profit potential"
            )

        elif profit >= 100:

            signals.append(
                "Healthy profit margin"
            )



        #
        # Demand Intelligence
        #

        if demand >= 75:

            signals.append(
                "High market demand"
            )



        #
        # Confidence Intelligence
        #

        if confidence >= 80:

            signals.append(
                "High confidence prediction"
            )



        #
        # Brand Intelligence
        #

        if product.brand:

            signals.append(
                f"Trusted brand: {product.brand}"
            )



        #
        # Historical Intelligence
        #

        historical_summary = None


        if historical:


            if historical.get("roi_improvement"):

                improvement = historical["roi_improvement"]


                if improvement > 0:

                    signals.append(
                        f"ROI improved {improvement:.2f}% compared to previous scans"
                    )


            if historical.get("previous_best_profit"):

                best_profit = historical["previous_best_profit"]


                if profit > best_profit:

                    signals.append(
                        "This is the best purchase opportunity recorded"
                    )



            historical_summary = {

                "previous_best_profit":
                    historical.get(
                        "previous_best_profit"
                    ),

                "average_previous_roi":
                    historical.get(
                        "average_previous_roi"
                    ),

                "roi_improvement":
                    historical.get(
                        "roi_improvement"
                    )

            }



        #
        # Final Explanation
        #

        explanation = (

            f"{action}: {product.name} "

            f"has ${profit:.0f} profit potential, "

            f"{roi:.0f}% ROI, "

            f"{demand}/100 demand score, "

            f"and {confidence}/100 market confidence."

        )



        if historical_summary:


            explanation += (

                " Historical analysis shows this deal "
                "compared against previous scans."

            )



        return {


            "explanation": explanation,

            "signals": signals,

            "historical": historical_summary

        }