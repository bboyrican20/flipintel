from sqlalchemy.orm import Session

from app.models.inventory import Inventory
from app.models.product import Product


class AnalyticsEngine:


    def portfolio_summary(
        self,
        db: Session
    ):

        inventory = db.query(Inventory).all()


        sold = [
            item for item in inventory
            if item.status == "SOLD"
        ]


        active = [
            item for item in inventory
            if item.status == "ACTIVE"
        ]


        capital = sum(
            item.purchase_price * (item.quantity or 1)
            for item in inventory
        )


        revenue = sum(
            item.sale_price or 0
            for item in sold
        )


        realized_profit = sum(
            item.actual_profit or 0
            for item in sold
        )


        projected_profit = sum(
            item.projected_profit or 0
            for item in active
        )


        roi = 0

        if capital:

            roi = round(
                (realized_profit / capital) * 100,
                2
            )


        return {

            "total_items": len(inventory),

            "sold_flips": len(sold),

            "active_inventory": len(active),

            "capital_invested": capital,

            "revenue_generated": revenue,

            "realized_profit": realized_profit,

            "projected_profit": projected_profit,

            "roi": roi

        }



    def best_flip(
        self,
        db: Session
    ):


        sold = (
            db.query(Inventory)
            .filter(
                Inventory.status == "SOLD"
            )
            .all()
        )


        if not sold:

            return None



        best = max(
            sold,
            key=lambda x:
                x.actual_profit or 0
        )


        product = (
            db.query(Product)
            .filter(
                Product.id == best.product_id
            )
            .first()
        )


        return {

            "product":
                product.name
                if product
                else None,

            "profit":
                best.actual_profit,

            "roi":
                best.actual_roi

        }



    def performance_summary(
        self,
        db: Session
    ):


        sold = (
            db.query(Inventory)
            .filter(
                Inventory.status == "SOLD"
            )
            .all()
        )


        if not sold:

            return {

                "total_sales": 0,

                "average_profit": 0,

                "average_roi": 0,

                "win_rate": 0

            }


        total_sales = len(sold)


        profits = sum(
            item.actual_profit or 0
            for item in sold
        )


        roi = sum(
            item.actual_roi or 0
            for item in sold
        )


        winners = [
            item for item in sold
            if (item.actual_profit or 0) > 0
        ]


        return {

            "total_sales":
                total_sales,

            "average_profit":
                round(
                    profits / total_sales,
                    2
                ),

            "average_roi":
                round(
                    roi / total_sales,
                    2
                ),

            "win_rate":
                round(
                    (len(winners) / total_sales) * 100,
                    2
                )

        }



    def brand_performance(
        self,
        db: Session
    ):


        inventory = (
            db.query(Inventory)
            .all()
        )


        brands = {}


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



            brand = product.brand or "Unknown"



            if brand not in brands:

                brands[brand] = {

                    "brand": brand,

                    "flips": 0,

                    "profit": 0,

                    "roi_total": 0

                }



            brands[brand]["flips"] += 1


            brands[brand]["profit"] += (
                item.actual_profit or
                item.projected_profit or
                0
            )


            brands[brand]["roi_total"] += (
                item.actual_roi or
                0
            )



        results = []


        for brand, data in brands.items():


            flips = data["flips"]


            results.append({

                "brand":
                    brand,

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
                    )

            })



        return sorted(
            results,
            key=lambda x:
                x["profit"],
            reverse=True
        )