from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.deal_ranker import get_top_deals


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)



@router.get("/top-deals")
def top_deals(
    db: Session = Depends(get_db)
):

    return {

        "top_deals":
            get_top_deals(db)

    }