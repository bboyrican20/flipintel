from fastapi import APIRouter

from app.db.database import SessionLocal
from app.models.inventory import Inventory


router = APIRouter(
    prefix="/sales",
    tags=["Sales"]
)



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


            "retailer": product.retailer,


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