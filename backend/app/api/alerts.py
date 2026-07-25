from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db

from app.services.alert_engine import alert_engine



router = APIRouter(

    prefix="/alerts",

    tags=["Alerts"]

)



#
# ALERT FEED
#

@router.get("/")
def get_alerts(

    db: Session = Depends(get_db)

):

    return alert_engine.generate_alerts(
        db
    )