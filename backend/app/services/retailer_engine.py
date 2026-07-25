from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.product import Product


class RetailerEngine:


    def retailer_performance(
        self,
        db: Session
    ):

        inventory = (
            db.query(Inventory)
            .all()
        )


        retailers = {}


        for item in inventory:


            product = (
                db.query(Product)
                .filter(
                    Product.id == item.product_id
                )
                .first()
            )


            if not product:

                continue


            retailer = (
                product.retailer
                or "Unknown"
            )


            if retailer not in retailers:

                retailers[retailer] = {

                    "retailer":
                        retailer,

                    "flips":
                        0,

                    "profit":
                        0,

                    "roi_total":
                        0,

                    "wins":
                        0

                }



            retailers[retailer]["flips"] += 1



            profit = (
                item.actual_profit
                if item.actual_profit is not None
                else item.projected_profit or 0
            )


            retailers[retailer]["profit"] += profit



            roi = (
                item.actual_roi
                if item.actual_roi is not None
                else 0
            )


            retailers[retailer]["roi_total"] += roi



            if profit > 0:

                retailers[retailer]["wins"] += 1



        results = []


        for retailer, data in retailers.items():


            flips = data["flips"]


            results.append({

                "retailer":
                    retailer,

                "flips":
                    flips,

                "profit":
                    round(
                        data["profit"],
                        2
                    ),

                "average_roi":
                    round(
                        data["roi_total"] / flips,
                        2
                    ),

                "win_rate":
                    round(
                        (data["wins"] / flips) * 100,
                        2
                    )

            })



        return sorted(

            results,

            key=lambda x:
                x["profit"],

            reverse=True

        )