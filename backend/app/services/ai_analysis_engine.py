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

            product.buy_price

            if product.buy_price is not None

            else (

                inventory.purchase_price

                if inventory

                else 0

            )

        )





        market_value = (

            product.market_price

            if product.market_price is not None

            else (

                product.sell_price

                if product.sell_price is not None

                else 0

            )

        )





        profit = (

            product.profit

            if product.profit is not None

            else market_value - buy_price

        )





        roi = (

            product.roi

            if product.roi is not None

            else (

                (profit / buy_price) * 100

                if buy_price > 0

                else 0

            )

        )





        discount = (

            ((market_value - buy_price) / market_value) * 100

            if market_value > 0

            else 0

        )







        # ==============================
        # SCORE ENGINE
        # ==============================


        profit_score = 50


        if profit >= 150:
            profit_score = 95

        elif profit >= 75:
            profit_score = 85

        elif profit > 0:
            profit_score = 70






        roi_score = 50


        if roi >= 200:
            roi_score = 100

        elif roi >= 100:
            roi_score = 90

        elif roi >= 50:
            roi_score = 75





        market_score = 80


        if market_value >= buy_price * 2:
            market_score = 92






        sell_speed_score = 85


        if product.sales_velocity == "HIGH":

            sell_speed_score = 95






        confidence = round(

            (

                profit_score +

                roi_score +

                market_score +

                sell_speed_score

            ) / 4

        )






        if confidence >= 85:

            recommendation = "STRONG BUY"

            risk = "LOW"


        elif confidence >= 70:

            recommendation = "BUY"

            risk = "MEDIUM"


        else:

            recommendation = "WATCH"

            risk = "HIGH"







        reasoning = [

            f"Bought {round(discount)}% below estimated market value",

            f"Projected profit opportunity of +${round(profit,2)}",

            f"ROI potential of {round(roi,2)}% exceeds FlipIntel targets"

        ]





        if product.brand:

            reasoning.append(

                f"{product.brand} has strong resale recognition"

            )





        if product.category:

            reasoning.append(

                f"{product.category} category shows resale demand"

            )







        # ==============================
        # SELLER ACTION PLAN
        # ==============================


        recommended_listing = round(

            market_value * 1.05,

            2

        )


        minimum_offer = round(

            market_value * .90,

            2

        )



        strategy = {


            "buy_price": round(buy_price,2),


            "target_sale_price": round(market_value,2),


            "recommended_listing": recommended_listing,


            "minimum_offer": minimum_offer,


            "expected_profit": round(profit,2),


            "strategy":

                "List slightly above market value and allow room for negotiation while protecting margin."

        }







        # ==============================
        # MARKETPLACE INTELLIGENCE
        # ==============================


        marketplace = {


            "sources": {

                "ebay": round(market_value * 1.02,2),

                "amazon": round(market_value * 1.08,2),

                "facebook": round(market_value * .95,2)

            },


            "market_price": round(market_value,2),


            "spread": round(

                market_value - buy_price,

                2

            ),


            "confidence": confidence

        }







        return {


            "product": product.name,


            "confidence": confidence,


            "score": confidence,


            "recommendation": recommendation,


            "risk": risk,


            "flip_window": "3-7 Days",



            "scores": {

                "profit": profit_score,

                "roi": roi_score,

                "market": market_score,

                "sell_speed": sell_speed_score

            },



            "metrics": {

                "purchase_price": round(buy_price,2),

                "expected_sale": round(market_value,2),

                "profit": round(profit,2),

                "roi": round(roi,2)

            },



            "reasoning": reasoning,


            "reasons": reasoning,


            "strategy": strategy,


            "marketplace": marketplace


        }





ai_analysis_engine = AIAnalysisEngine()