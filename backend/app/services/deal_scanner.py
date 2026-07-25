from sqlalchemy.orm import Session

from app.models.product import Product

from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine



class DealScanner:


    def __init__(self):

        self.flip_engine = FlipScoreEngine()

        self.buy_engine = BuyPriceEngine()



    def scan(
        self,
        db: Session,
        minimum_score: int = 70
    ):


        products = (
            db.query(Product)
            .all()
        )


        opportunities = []


        for product in products:


            try:

                score = (
                    self.flip_engine
                    .calculate_score(
                        product.id,
                        db
                    )
                )


                buy = (
                    self.buy_engine
                    .calculate(
                        product.id,
                        db
                    )
                )



                if score["flip_score"] >= minimum_score:


                    opportunities.append({

                        "product":
                            product.name,


                        "retailer":
                            product.retailer,


                        "buy_price":
                            buy["current_buy_price"],


                        "market_price":
                            buy["market_price"],


                        "profit":
                            buy["expected_profit"],


                        "roi":
                            round(
                                (
                                    buy["expected_profit"]
                                    /
                                    buy["current_buy_price"]
                                )
                                *
                                100,
                                2
                            ),


                        "flip_score":
                            score["flip_score"],


                        "decision":
                            score["decision"]

                    })


            except Exception:


                continue



        opportunities.sort(

            key=lambda x:
                x["flip_score"],

            reverse=True

        )


        return {


            "deals_found":
                len(opportunities),


            "opportunities":
                opportunities

        }