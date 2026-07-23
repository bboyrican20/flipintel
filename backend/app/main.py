from fastapi import FastAPI

from app.db.database import engine, Base

# Import models so SQLAlchemy knows them
from app.models.product import Product
from app.models.deal_analysis import DealAnalysis

from app.api.products import router as products_router
from app.api.analysis import router as analysis_router


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FlipIntel API",
    description="Retail intelligence platform for resellers",
    version="0.1.0"
)


# Register API routes
app.include_router(products_router)
app.include_router(analysis_router)


@app.get("/")
def home():
    return {
        "name": "FlipIntel",
        "status": "online",
        "version": "0.1.0"
    }


@app.get("/health")
def health():
    return {
        "healthy": True
    }