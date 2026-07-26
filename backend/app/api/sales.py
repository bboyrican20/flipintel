from fastapi import APIRouter
from pydantic import BaseModel

from datetime import datetime

from app.db.database import SessionLocal
from app.models.inventory import Inventory


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)



class SaleRequest(BaseModel):

    sale_price: float





@router.get("/")
def get_sales():


    db = SessionLocal()


    sold_items = db.query(Inventory).filter(

        Inventory.status == "SOLD"

    ).all()



    sales = []



    for item in sold_items:


        product = item.product


        sales.append({


            "inventory_id": item.id,

            "product": product.name,

            "brand": product.brand,

            "category": product.category,

            "retailer": item.retailer,

            "purchase_price": item.purchase_price,

            "sale_price": item.sale_price,

            "profit": item.actual_profit,

            "roi": item.actual_roi,

            "sold_at": item.sold_at,

            "status": "COMPLETED"


        })



    db.close()



    return {


        "total_sales": len(sales),

        "sales": sales


    }








@router.post("/{inventory_id}")
def sell_inventory_item(

    inventory_id: int,

    sale: SaleRequest

):


    db = SessionLocal()



    item = db.query(Inventory).filter(

        Inventory.id == inventory_id

    ).first()



    if not item:


        db.close()


        return {


            "error": "Inventory item not found"

        }





    item.sale_price = sale.sale_price


    item.actual_profit = (

        sale.sale_price -

        item.purchase_price

    )



    if item.purchase_price:


        item.actual_roi = round(

            (

                item.actual_profit /

                item.purchase_price

            ) * 100,

            2

        )



    item.status = "SOLD"


    item.sold_at = datetime.utcnow()



    db.commit()


    db.refresh(item)


    db.close()



    return {


        "message": "Item sold successfully",


        "inventory_id": inventory_id,


        "profit": item.actual_profit,


        "roi": item.actual_roi


    }