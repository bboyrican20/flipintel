from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


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
from app.api import history
from app.api import inventory
from app.api import analytics
from app.api import deals
from app.api import alerts
from app.api import sales
from app.api import ai_analysis
from app.api import flip_strategy
from app.api import deal_ai



app = FastAPI(

    title="FlipIntel",

    description="AI Powered Product Flipping Intelligence Platform",

    version="1.0.0"

)





# Allow React frontend to communicate with FastAPI

app.add_middleware(

    CORSMiddleware,

    allow_origins=[

        "http://localhost:5173"

    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],

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
# Rankings
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
# Market Intelligence
#

app.include_router(
    market_intelligence.router
)





#
# Product History
#

app.include_router(
    history.router
)





#
# Inventory
#

app.include_router(
    inventory.router
)





#
# Analytics
#

app.include_router(
    analytics.router
)





#
# Deals
#

app.include_router(
    deals.router
)





#
# Alerts
#

app.include_router(
    alerts.router
)





#
# Sales Intelligence
#

app.include_router(
    sales.router
)





#
# AI Analysis
#

app.include_router(
    ai_analysis.router
)





#
# Flip Strategy Engine
#

app.include_router(
    flip_strategy.router
)





#
# Deal AI Engine
#

app.include_router(
    deal_ai.router
)