from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.ai_analysis_engine import ai_analysis_engine


router = APIRouter(
    prefix="/ai",
    tags=["AI Analysis"]
)



@router.get("/{product_id}")
def analyze_product(
    product_id:int,
    db:Session = Depends(get_db)
):

    return ai_analysis_engine.analyze(
        product_id,
        db
    )