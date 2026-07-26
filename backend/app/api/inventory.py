from fastapi import APIRouter
from pydantic import BaseModel

from app.db.database import SessionLocal

from app.models.inventory import Inventory
from app.models.product import Product


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)



class InventoryCreate(BaseModel):

    product_id: int | None = None

    product: str

    retailer: str

    purchase_price: float

    expected_sale_price: float

    projected_profit: float





@router.get("/")
def get_inventory():

    db = SessionLocal()


    items = db.query(Inventory).all()


    result = []


    for item in items:


        product = (
            db.query(Product)
            .filter(
                Product.id == item.product_id
            )
            .first()
        )


        result.append({

            "inventory_id": item.id,

            "product": product.name if product else "Unknown",

            "brand": product.brand if product else None,

            "category": product.category if product else None,

            "retailer": item.retailer or "Unknown",

            "purchase_price": item.purchase_price,

            "buy_price": item.purchase_price,

            "expected_sale_price": item.expected_sale_price,

            "market_price": item.expected_sale_price,

            "projected_profit": item.projected_profit,

            "profit": item.projected_profit,

            "sale_price": item.sale_price,

            "actual_profit": item.actual_profit,

            "actual_roi": item.actual_roi,

            "status": item.status

        })



    db.close()



    return {

        "total_items": len(result),

        "inventory": result

    }







@router.post("/")
def add_inventory(
    item: InventoryCreate
):

    db = SessionLocal()



    #
    # FIND PRODUCT
    #

    if item.product_id:


        product = (

            db.query(Product)

            .filter(

                Product.id == item.product_id

            )

            .first()

        )


    else:


        product = (

            db.query(Product)

            .filter(

                Product.name == item.product

            )

            .first()

        )





    if not product:


        db.close()


        return {

            "error":

            "Product not found"

        }





    #
    # CREATE INVENTORY ITEM
    #

    new_item = Inventory(

        product_id=product.id,

        retailer=item.retailer,

        purchase_price=item.purchase_price,

        expected_sale_price=item.expected_sale_price,

        projected_profit=item.projected_profit,

        status="ACTIVE"

    )



    db.add(new_item)


    db.commit()


    db.refresh(new_item)



    db.close()



    return {


        "message":

        "Added to inventory",


        "inventory_id":

        new_item.id


    }