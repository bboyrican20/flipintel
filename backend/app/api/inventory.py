from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.inventory import Inventory
from app.models.product import Product


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"]
)


#
# ADD INVENTORY
#

@router.post("/add")
def add_inventory(
    data: dict,
    db: Session = Depends(get_db)
):

    product_id = data["product_id"]
    quantity = data.get("quantity", 1)
    purchase_price = data["purchase_price"]


    product = (
        db.query(Product)
        .filter(
            Product.id == product_id
        )
        .first()
    )


    if not product:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )


    expected_sale_price = (
        product.market_price
        or product.sell_price
        or 0
    )


    projected_profit = (
        expected_sale_price - purchase_price
    ) * quantity



    inventory = Inventory(

        product_id=product.id,

        quantity=quantity,

        purchase_price=purchase_price,

        expected_sale_price=expected_sale_price,

        projected_profit=projected_profit,

        status="ACTIVE"

    )


    db.add(inventory)

    db.commit()

    db.refresh(inventory)



    return {

        "inventory_id": inventory.id,

        "product": product.name,

        "units_added": quantity,

        "capital_invested":
            purchase_price * quantity,

        "expected_revenue":
            expected_sale_price * quantity,

        "projected_profit":
            projected_profit,

        "status":
            inventory.status

    }



#
# GET INVENTORY
#

@router.get("/")
def get_inventory(
    db: Session = Depends(get_db)
):

    inventory = (
        db.query(Inventory)
        .all()
    )


    results = []


    for item in inventory:

        product = (
            db.query(Product)
            .filter(
                Product.id == item.product_id
            )
            .first()
        )


        results.append({

            "inventory_id": item.id,

            "product":
                product.name
                if product
                else None,

            "quantity":
                item.quantity,

            "purchase_price":
                item.purchase_price,

            "expected_sale_price":
                item.expected_sale_price,

            "projected_profit":
                item.projected_profit,

            "status":
                item.status

        })


    return {

        "total_items":
            len(results),

        "inventory":
            results

    }



#
# PORTFOLIO SUMMARY
#

@router.get("/portfolio")
def portfolio(
    db: Session = Depends(get_db)
):

    inventory = (
        db.query(Inventory)
        .all()
    )


    capital = sum(
        item.purchase_price *
        (item.quantity or 1)
        for item in inventory
    )


    revenue = sum(
        item.expected_sale_price *
        (item.quantity or 1)
        for item in inventory
    )


    profit = sum(
        item.projected_profit or 0
        for item in inventory
    )


    return {

        "inventory_count":
            len(inventory),

        "capital_invested":
            capital,

        "projected_revenue":
            revenue,

        "projected_profit":
            profit

    }