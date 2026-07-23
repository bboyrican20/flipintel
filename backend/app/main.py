from fastapi import FastAPI

from app.db.database import engine, Base
from app.api.products import router as products_router

# Import models so SQLAlchemy registers them
from app.models.product import Product


# Create database tables
Base.metadata.create_all(bind=engine)


app = FastAPI(
    title="FlipIntel API",
    description="Retail intelligence platform for resellers",
    version="0.1.0"
)


# Register API routes
app.include_router(products_router)


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