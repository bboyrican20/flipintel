from sqlalchemy.orm import Session

from app.models.product import Product


class ProductRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_by_barcode(self, barcode: str):

        return (
            self.db.query(Product)
            .filter(Product.barcode == barcode)
            .first()
        )

    def create_product(
        self,
        lookup: dict,
        buy_price: float,
        retailer: str
    ):

        market_price = lookup["market_price"]

        profit = market_price - buy_price

        roi = (
            (profit / buy_price) * 100
            if buy_price > 0
            else 0
        )

        product = Product(

            name=lookup["name"],

            brand=lookup["brand"],

            category=lookup["category"],

            barcode=lookup["barcode"],

            retailer=retailer,

            buy_price=buy_price,

            sell_price=market_price,

            market_price=market_price,

            profit=profit,

            roi=roi,

            image=lookup.get("image"),

            sales_velocity="HIGH"

        )

        self.db.add(product)

        self.db.commit()

        self.db.refresh(product)

        return product

    def update_existing_product(
        self,
        product: Product,
        lookup: dict,
        buy_price: float
    ):

        market_price = lookup["market_price"]

        product.name = lookup["name"]

        product.brand = lookup["brand"]

        product.category = lookup["category"]

        product.retailer = retailer = product.retailer

        product.buy_price = buy_price

        product.sell_price = market_price

        product.market_price = market_price

        product.image = lookup.get("image")

        product.profit = market_price - buy_price

        product.roi = (
            (product.profit / buy_price) * 100
            if buy_price > 0
            else 0
        )

        self.db.commit()

        self.db.refresh(product)

        return product

    def get(self, product_id: int):

        return (
            self.db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )