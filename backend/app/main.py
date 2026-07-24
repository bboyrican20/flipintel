from fastapi import FastAPI

from app.api import products
from app.api import analysis
from app.api import market_data
from app.api import scanner
from app.api import reports
from app.api import opportunities
from app.api import dashboard
from app.api import rankings
from app.api import action_center
from app.api import market_intelligence


app = FastAPI(

    title="FlipIntel",

    description="AI Powered Product Flipping Intelligence Platform",

    version="1.0.0"

)



@app.get("/")
def root():

    return {

        "app": "FlipIntel",

        "status": "running",

        "version": "1.0.0"

    }



#
# Product Routes
#

app.include_router(
    products.router
)



#
# Analysis Engine
#

app.include_router(
    analysis.router
)



#
# Market Data
#

app.include_router(
    market_data.router
)



#
# Barcode Scanner
#

app.include_router(
    scanner.router
)



#
# Reports
#

app.include_router(
    reports.router
)



#
# Opportunities
#

app.include_router(
    opportunities.router
)



#
# Dashboard
#

app.include_router(
    dashboard.router
)



#
# Deal Rankings
#

app.include_router(
    rankings.router
)



#
# Action Center
#

app.include_router(
    action_center.router
)



#
# Market Intelligence Engine
#

app.include_router(
    market_intelligence.router
)