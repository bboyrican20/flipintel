from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.deal_feed_engine import deal_feed_engine



router = APIRouter(

    prefix="/deals",

    tags=["Deals"]

)



#
# DEAL FEED
#

@router.get("/feed")
def deal_feed(

    db: Session = Depends(get_db)

):

    return deal_feed_engine.generate_feed(
        db
    )