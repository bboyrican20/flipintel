from sqlalchemy.orm import Session

from app.models.product import Product



def find_existing_product(
    db: Session,
    barcode=None,
    upc=None,
    sku=None
):


    query = db.query(Product)


    if barcode:

        product = (
            query
            .filter(
                Product.barcode == barcode
            )
            .first()
        )

        if product:
            return product



    if upc:

        product = (
            query
            .filter(
                Product.upc == upc
            )
            .first()
        )

        if product:
            return product



    if sku:

        product = (
            query
            .filter(
                Product.sku == sku
            )
            .first()
        )

        if product:
            return product



    return None