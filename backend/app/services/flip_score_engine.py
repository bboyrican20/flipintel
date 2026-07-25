from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.product import Product
from app.models.scan_history import ScanHistory



class FlipScoreEngine:


    def calculate_score(
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

                "error":
                    "Product not found"

            }



        #
        # Profit Score
        #

        profit_score = 0

        profit = (
            product.market_price or 0
        ) - (
            product.buy_price or 0
        )


        if profit >= 200:

            profit_score = 30

        elif profit >= 100:

            profit_score = 25

        elif profit >= 50:

            profit_score = 15

        else:

            profit_score = 5



        #
        # ROI Score
        #

        roi_score = 0


        if product.buy_price:

            roi = (
                profit /
                product.buy_price
            ) * 100

        else:

            roi = 0



        if roi >= 150:

            roi_score = 25

        elif roi >= 75:

            roi_score = 20

        elif roi >= 30:

            roi_score = 12

        else:

            roi_score = 5



        #
        # Brand Score
        #

        brand_score = 10


        brand = (
            product.brand
            or ""
        ).lower()


        premium_brands = [

            "milwaukee",
            "dewalt",
            "makita",
            "bosch",
            "festool"

        ]


        if brand in premium_brands:

            brand_score = 20



        #
        # History Score
        #

        history_score = 0


        history = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product_id
            )
            .count()
        )


        if history >= 10:

            history_score = 15

        elif history >= 5:

            history_score = 10

        elif history > 0:

            history_score = 5



        #
        # Risk Score
        #

        risk_score = 10


        if history == 0:

            risk_score = 5



        total_score = (

            profit_score +

            roi_score +

            brand_score +

            history_score +

            risk_score

        )



        if total_score >= 85:

            decision = "BUY NOW"

        elif total_score >= 70:

            decision = "CONSIDER"

        elif total_score >= 50:

            decision = "RESEARCH"

        else:

            decision = "PASS"



        return {


            "product":
                product.name,


            "flip_score":
                total_score,


            "decision":
                decision,


            "breakdown":
                {

                    "profit_score":
                        profit_score,

                    "roi_score":
                        roi_score,

                    "brand_score":
                        brand_score,

                    "history_score":
                        history_score,

                    "risk_score":
                        risk_score

                },


            "metrics":
                {

                    "estimated_profit":
                        round(profit,2),

                    "estimated_roi":
                        round(roi,2)

                },


            "recommendation":

                f"{decision}: {product.name} scored {total_score}/100"

        }