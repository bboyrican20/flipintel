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



            #
            # HOT DEAL
            #

            if (
                score >= 75
                and profit >= 50
                and roi >= 75
            ):


                alerts.append({

                    "type":
                        "HOT DEAL",

                    "priority":
                        "HIGH",

                    "product_id":
                        product.id,

                    "product":
                        product.name,

                    "message":
                        f"🔥 Strong flip opportunity - ${round(profit,2)} projected profit at {round(roi,2)}% ROI",

                    "score":
                        score,

                    "profit":
                        profit,

                    "roi":
                        roi

                })



            #
            # WATCH LIST
            #

            elif score >= 55:


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
                        f"Monitor {product.name} - {round(roi,2)}% ROI opportunity",

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