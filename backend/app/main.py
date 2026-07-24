from fastapi import FastAPI

from app.db.database import engine, Base


from app.models.product import Product
from app.models.deal_analysis import DealAnalysis
from app.models.market_data import MarketData
from app.models.scan_history import ScanHistory



from app.api.products import router as product_router
from app.api.analysis import router as analysis_router
from app.api.reports import router as reports_router
from app.api.opportunities import router as opportunities_router
from app.api.scanner import router as scanner_router
from app.api.market_data import router as market_data_router
from app.api.dashboard import router as dashboard_router
from app.api.rankings import router as rankings_router



Base.metadata.create_all(
    bind=engine
)



app = FastAPI(

    title="FlipIntel API",

    description="Retail intelligence platform for resellers",

    version="0.1.0"

)



app.include_router(product_router)

app.include_router(analysis_router)

app.include_router(reports_router)

app.include_router(opportunities_router)

app.include_router(scanner_router)

app.include_router(market_data_router)

app.include_router(dashboard_router)

app.include_router(rankings_router)



@app.get("/")
def home():

    return {

        "name": "FlipIntel",

        "status": "online"

    }



@app.get("/health")
def health():

    return {

        "healthy": True

    }