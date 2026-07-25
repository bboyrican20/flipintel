from sqlalchemy.orm import Session

from app.models.product import Product

from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine



class AlertEngine:


    def __init__(self):

        self.flip_engine = FlipScoreEngine()

        self.buy_engine = BuyPriceEngine()



    def generate_alerts(
        self,
        db: Session
    ):


        products = (
            db.query(Product)
            .all()
        )


        alerts = []



        for product in products:


            flip = self.flip_engine.calculate_score(
                product.id,
                db
            )


            buy = self.buy_engine.calculate(
                product.id,
                db
            )


            if "error" in flip:
                continue


            if "error" in buy:
                continue



            score = flip["flip_score"]

            profit = buy["expected_profit"]

            roi = flip["metrics"]["estimated_roi"]



            if (
                score >= 85
                and profit >= 200
                and roi >= 100
            ):

                alerts.append({

                    "type":
                        "HOT_DEAL",

                    "priority":
                        "HIGH",

                    "product_id":
                        product.id,

                    "product":
                        product.name,

                    "message":
                        f"BUY NOW - ${round(profit,2)} profit opportunity at {round(roi,2)}% ROI",

                    "score":
                        score,

                    "profit":
                        profit,

                    "roi":
                        roi

                })



            elif score >= 65:


                alerts.append({

                    "type":
                        "WATCH",

                    "priority":
                        "MEDIUM",

                    "product_id":
                        product.id,

                    "product":
                        product.name,

                    "message":
                        "Opportunity worth monitoring",

                    "score":
                        score,

                    "profit":
                        profit,

                    "roi":
                        roi

                })



        alerts.sort(

            key=lambda x:
                x["score"],

            reverse=True

        )


        return {

            "total_alerts":
                len(alerts),

            "alerts":
                alerts

        }



alert_engine = AlertEngine()