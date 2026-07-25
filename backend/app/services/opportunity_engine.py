from sqlalchemy.orm import Session

from app.models.product import Product
from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine


class OpportunityEngine:


    def __init__(self):

        self.flip_engine = FlipScoreEngine()
        self.buy_engine = BuyPriceEngine()



    def get_opportunities(
        self,
        db: Session
    ):


        products = (
            db.query(Product)
            .all()
        )


        opportunities = []


        for product in products:


            flip_score = (
                self.flip_engine.calculate_score(
                    product.id,
                    db
                )
            )


            buy_price = (
                self.buy_engine.calculate(
                    product.id,
                    db
                )
            )


            if "error" in flip_score:
                continue


            if "error" in buy_price:
                continue



            if flip_score["decision"] in [
                "BUY NOW",
                "CONSIDER"
            ]:


                opportunities.append({

                    "product_id":
                        product.id,

                    "product":
                        product.name,

                    "retailer":
                        product.retailer,

                    "flip_score":
                        flip_score["flip_score"],

                    "decision":
                        flip_score["decision"],

                    "current_buy_price":
                        buy_price["current_buy_price"],

                    "max_buy_price":
                        buy_price["max_buy_price"],

                    "market_price":
                        buy_price["market_price"],

                    "expected_profit":
                        buy_price["expected_profit"],

                    "roi":
                        flip_score["metrics"]["estimated_roi"]

                })



        opportunities.sort(
            key=lambda x:
                x["flip_score"],
            reverse=True
        )


        return {


            "total_opportunities":
                len(opportunities),


            "opportunities":
                opportunities

        }



opportunity_engine = OpportunityEngine()