from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.product import Product
from app.services.marketplace_engine import MarketplaceEngine



router = APIRouter(

    prefix="/marketplace",

    tags=["Marketplace Intelligence"]

)





@router.get("/{product_id}")

def marketplace_analysis(

    product_id:int,

    db:Session = Depends(get_db)

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

            "error":"Product not found"

        }



    engine = MarketplaceEngine()



    return {


        "product":

            product.name,


        "marketplace":

            engine.analyze(product)

    }