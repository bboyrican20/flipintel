from sqlalchemy.orm import Session

from app.models.product import Product

from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine
from app.services.confidence_engine import calculate_confidence


class DealFeedEngine:


    def __init__(self):

        self.flip_engine = FlipScoreEngine()

        self.buy_engine = BuyPriceEngine()



    def generate_feed(
        self,
        db: Session
    ):


        products = (
            db.query(Product)
            .all()
        )


        hot_deals = []

        watch_list = []

        passes = []



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



            confidence = calculate_confidence(
                product,
                None
            )



            score = flip["flip_score"]


            reasons = []



            if flip["metrics"]["estimated_profit"] >= 200:

                reasons.append(
                    "Large profit spread"
                )


            if flip["metrics"]["estimated_roi"] >= 100:

                reasons.append(
                    "Exceptional ROI"
                )


            if product.brand:

                reasons.append(
                    f"Premium brand: {product.brand}"
                )



            if confidence["confidence"] >= 90:

                reasons.append(
                    "High confidence"
                )



            deal = {


                "product_id":
                    product.id,


                "product":
                    product.name,


                "retailer":
                    product.retailer,


                "score":
                    score,


                "decision":
                    flip["decision"],


                "buy_price":
                    buy["current_buy_price"],


                "market_price":
                    buy["market_price"],


                "profit":
                    buy["expected_profit"],


                "roi":
                    flip["metrics"]["estimated_roi"],


                "confidence":
                    confidence["confidence"],


                "reasons":
                    reasons

            }



            if score >= 85:

                hot_deals.append(deal)


            elif score >= 65:

                watch_list.append(deal)


            else:

                passes.append(deal)



        hot_deals.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        watch_list.sort(
            key=lambda x: x["score"],
            reverse=True
        )


        return {


            "hot_deals":
                hot_deals,


            "watch_list":
                watch_list,


            "passes":
                passes,


            "summary":
                {

                    "total_products":
                        len(products),

                    "hot_deals":
                        len(hot_deals),

                    "watching":
                        len(watch_list),

                    "passed":
                        len(passes)

                }

        }



deal_feed_engine = DealFeedEngine()