from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.services.opportunity_engine import opportunity_engine


router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"]
)



#
# OPPORTUNITY ENGINE
#

@router.get("/")
def get_opportunities(
    db: Session = Depends(get_db)
):

    result = (
        opportunity_engine.get_opportunities(
            db
        )
    )


    return result