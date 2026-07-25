from sqlalchemy.orm import Session

from app.models.product import Product



class BuyPriceEngine:


    def calculate(
        self,
        product_id: int,
        db: Session,
        target_roi: float = 50
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



        market_price = (
            product.market_price
            or product.sell_price
            or 0
        )


        current_buy_price = (
            product.buy_price
            or 0
        )



        if market_price <= 0:

            return {

                "error":
                    "No market price available"

            }



        #
        # Formula:
        #
        # ROI = Profit / Cost
        #
        # Max Buy =
        # Sale Price / (1 + ROI)
        #

        max_buy_price = (
            market_price /
            (1 + (target_roi / 100))
        )



        expected_profit = (
            market_price -
            current_buy_price
        )



        margin = (
            max_buy_price -
            current_buy_price
        )



        if current_buy_price <= max_buy_price:

            decision = "BUY"

        else:

            decision = "PASS"



        return {


            "product":
                product.name,


            "market_price":
                round(
                    market_price,
                    2
                ),


            "current_buy_price":
                round(
                    current_buy_price,
                    2
                ),


            "target_roi":
                target_roi,


            "max_buy_price":
                round(
                    max_buy_price,
                    2
                ),


            "purchase_margin":
                round(
                    margin,
                    2
                ),


            "expected_profit":
                round(
                    expected_profit,
                    2
                ),


            "decision":
                decision


        }