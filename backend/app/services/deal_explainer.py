class DealExplainer:


    def explain(
        self,
        product,
        profit,
        roi,
        demand,
        confidence,
        action
    ):


        signals = []


        if roi >= 100:
            signals.append(
                "Excellent ROI"
            )

        elif roi >= 50:
            signals.append(
                "Strong ROI"
            )


        if profit >= 200:
            signals.append(
                "High profit opportunity"
            )


        if demand >= 75:
            signals.append(
                "High market demand"
            )


        if confidence >= 80:
            signals.append(
                "Strong market confidence"
            )


        if product.brand:
            signals.append(
                f"Trusted brand: {product.brand}"
            )



        explanation = (
            f"{action}: {product.name} "
            f"has ${profit:.0f} profit potential, "
            f"{roi:.0f}% ROI, "
            f"{demand}/100 demand score, "
            f"and {confidence}/100 market confidence."
        )


        return {

            "explanation": explanation,

            "signals": signals

        }