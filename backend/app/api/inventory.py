from fastapi import APIRouter, HTTPException
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





class InventorySale(BaseModel):

    sale_price: float





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


            "status": getattr(
                item,
                "status",
                "AVAILABLE"
            )


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



    new_item = Inventory(


        product=item.product,


        purchase_price=item.purchase_price,


        expected_sale_price=item.expected_sale_price,


        projected_profit=item.projected_profit


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










@router.post("/{inventory_id}/sell")
def sell_inventory(

    inventory_id: int,

    sale: InventorySale

):


    db = SessionLocal()



    item = db.query(Inventory).filter(

        Inventory.id == inventory_id

    ).first()



    if not item:


        db.close()


        raise HTTPException(

            status_code=404,

            detail="Inventory item not found"

        )




    item.status = "SOLD"



    item.sale_price = sale.sale_price




    item.actual_profit = (

        sale.sale_price -

        item.purchase_price

    )




    db.commit()



    db.refresh(item)



    db.close()




    return {


        "message":
        "Inventory item sold",


        "inventory_id":
        inventory_id,


        "sale_price":
        sale.sale_price,


        "profit":
        item.actual_profit,


        "status":
        item.status


    }