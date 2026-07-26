from sqlalchemy.orm import Session

from app.models.product import Product
from app.models.inventory import Inventory


class AIAnalysisEngine:


    def analyze(
        self,
        product_id: int,
        db: Session
    ):


        product = (
            db.query(Product)
            .filter(
                Product.id == product_id
            )
            .first()
        )


        if not product:

            return {
                "error": "Product not found"
            }



        inventory = (
            db.query(Inventory)
            .filter(
                Inventory.product_id == product_id
            )
            .first()
        )



        buy_price = (
            inventory.purchase_price
            if inventory
            else product.buy_price or 0
        )


        sale_price = (
            inventory.expected_sale_price
            if inventory
            else product.market_price or 0
        )



        profit = sale_price - buy_price



        roi = 0

        if buy_price > 0:

            roi = (
                profit / buy_price
            ) * 100



        score = 50



        reasons = []



        if profit >= 50:

            score += 15

            reasons.append(
                f"Strong profit opportunity (${round(profit,2)})"
            )



        if roi >= 100:

            score += 20

            reasons.append(
                f"High ROI potential ({round(roi,2)}%)"
            )



        if product.brand:

            score += 5

            reasons.append(
                f"{product.brand} has resale recognition"
            )



        if product.category:

            reasons.append(
                f"{product.category} market demand considered"
            )



        if score >= 85:

            recommendation = "STRONG BUY"

            risk = "LOW"



        elif score >= 70:

            recommendation = "BUY"

            risk = "MEDIUM"



        else:

            recommendation = "WATCH"

            risk = "HIGH"




        confidence = min(score,100)



        return {

            "product": product.name,

            "score": score,

            "confidence": confidence,

            "recommendation": recommendation,

            "risk": risk,

            "flip_window": "3-7 Days",

            "metrics": {

                "purchase_price": buy_price,

                "expected_sale": sale_price,

                "profit": round(profit,2),

                "roi": round(roi,2)

            },

            "reasons": reasons

        }



ai_analysis_engine = AIAnalysisEngine()