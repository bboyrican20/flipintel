class DealIntelligence:


    def calculate_score(
        self,
        profit,
        roi,
        confidence,
        demand_score,
        market_confidence
    ):


        score = 0


        # Profit Weight
        if profit >= 200:
            score += 100
        elif profit >= 100:
            score += 75
        elif profit >= 50:
            score += 50



        # ROI Weight
        if roi >= 100:
            score += 100
        elif roi >= 75:
            score += 75
        elif roi >= 50:
            score += 50



        # Confidence
        score += confidence



        # Market Demand
        score += demand_score



        # Market Confidence
        score += market_confidence



        return score



    def recommendation(
        self,
        score
    ):


        if score >= 400:

            return "STRONG BUY"


        if score >= 300:

            return "BUY"


        if score >= 200:

            return "WATCH"


        return "AVOID"