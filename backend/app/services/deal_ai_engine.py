from app.services.ai_analysis_engine import AIAnalysisEngine


class DealAIEngine:

    def __init__(self):
        self.ai = AIAnalysisEngine()

    def explain(self, product_id, db):

        analysis = self.ai.analyze(product_id, db)

        if "error" in analysis:
            return analysis

        metrics = analysis["metrics"]

        reasons = []

        if metrics["roi"] >= 150:
            reasons.append(
                f"Excellent ROI ({metrics['roi']:.2f}%)"
            )
        elif metrics["roi"] >= 100:
            reasons.append(
                f"Strong ROI ({metrics['roi']:.2f}%)"
            )

        if metrics["profit"] >= 200:
            reasons.append(
                f"High profit opportunity (${metrics['profit']:.2f})"
            )
        elif metrics["profit"] >= 100:
            reasons.append(
                f"Solid projected profit (${metrics['profit']:.2f})"
            )

        if analysis["risk"] == "LOW":
            reasons.append(
                "Low investment risk"
            )

        return {
            "product": analysis["product"],
            "score": analysis["score"],
            "confidence": analysis["confidence"],
            "recommendation": analysis["recommendation"],
            "risk": analysis["risk"],
            "flip_window": analysis["flip_window"],
            "buy_price": metrics["purchase_price"],
            "market_price": metrics["expected_sale"],
            "profit": metrics["profit"],
            "roi": metrics["roi"],
            "reasons": reasons
        }


deal_ai_engine = DealAIEngine()