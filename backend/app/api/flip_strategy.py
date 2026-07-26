from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.models.product import Product

from app.services.flip_strategy_engine import FlipStrategyEngine



router = APIRouter(

    prefix="/flip-strategy",

    tags=["Flip Strategy"]

)





@router.get("/{product_id}")

def get_flip_strategy(

    product_id: int,

    db: Session = Depends(get_db)

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

            "error": "Product not found"

        }




    engine = FlipStrategyEngine()



    strategy = engine.generate_strategy(

        product

    )



    return {


        "product":

            product.name,


        "strategy":

            strategy

    }