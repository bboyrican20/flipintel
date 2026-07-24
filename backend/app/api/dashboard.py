from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from app.db.database import get_db
from app.models.product import Product
from app.models.scan_history import ScanHistory


router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"]
)


@router.get("/summary")
def dashboard_summary(
    db: Session = Depends(get_db)
):

    total_products = (
        db.query(Product)
        .count()
    )


    total_scans = (
        db.query(ScanHistory)
        .count()
    )


    strong_buys = (
        db.query(ScanHistory)
        .filter(
            ScanHistory.recommendation == "STRONG BUY"
        )
        .count()
    )


    average_roi = (
        db.query(
            func.avg(Product.roi)
        )
        .scalar()
    )


    total_profit = (
        db.query(
            func.sum(Product.profit)
        )
        .scalar()
    )


    return {

        "total_products":
            total_products,

        "total_scans":
            total_scans,

        "strong_buys":
            strong_buys,

        "average_roi":
            round(average_roi or 0, 2),

        "total_profit_opportunity":
            round(total_profit or 0, 2)

    }



@router.get("/brands")
def brand_intelligence(
    db: Session = Depends(get_db)
):

    results = (
        db.query(
            Product.brand,
            func.avg(Product.roi),
            func.count(Product.id)
        )
        .filter(
            Product.brand != None
        )
        .group_by(
            Product.brand
        )
        .all()
    )


    brands = []


    for brand, avg_roi, count in results:

        brands.append({

            "brand": brand,

            "average_roi":
                round(avg_roi or 0, 2),

            "products":
                count

        })


    return {
        "top_brands": brands
    }



@router.get("/categories")
def category_intelligence(
    db: Session = Depends(get_db)
):

    results = (
        db.query(
            Product.category,
            func.avg(Product.roi),
            func.count(Product.id)
        )
        .filter(
            Product.category != None
        )
        .group_by(
            Product.category
        )
        .all()
    )


    categories = []


    for category, avg_roi, count in results:

        categories.append({

            "category":
                category,

            "average_roi":
                round(avg_roi or 0, 2),

            "products":
                count

        })


    return {
        "categories": categories
    }