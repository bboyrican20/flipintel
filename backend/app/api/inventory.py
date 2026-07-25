from fastapi import APIRouter
from pydantic import BaseModel

from app.db.database import SessionLocal

from app.models.inventory import Inventory


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)



class InventoryCreate(BaseModel):

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


        result.append({

            "inventory_id": item.id,

            "product": item.product,

            "purchase_price": item.purchase_price,

            "expected_sale_price": item.expected_sale_price,

            "projected_profit": item.projected_profit,

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

    from app.models.product import Product



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