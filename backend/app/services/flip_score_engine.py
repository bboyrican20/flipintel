from sqlalchemy.orm import Session

from app.models.product import Product

from app.engines.profit_engine import ProfitEngine
from app.engines.roi_engine import ROIEngine
from app.engines.brand_engine import BrandEngine
from app.engines.history_engine import HistoryEngine
from app.engines.risk_engine import RiskEngine
from app.engines.demand_engine import DemandEngine
from app.engines.competition_engine import CompetitionEngine
from app.engines.confidence_engine import ConfidenceEngine
from app.engines.category_engine import CategoryEngine


class FlipScoreEngine:

    def __init__(self):

        self.profit = ProfitEngine()
        self.roi = ROIEngine()
        self.brand = BrandEngine()
        self.history = HistoryEngine()
        self.risk = RiskEngine()

        # Future AI engines
        self.demand = DemandEngine()
        self.competition = CompetitionEngine()
        self.confidence = ConfidenceEngine()
        self.category = CategoryEngine()

    def calculate_score(
        self,
        product_id: int,
        db: Session
    ):

        product = (
            db.query(Product)
            .filter(Product.id == product_id)
            .first()
        )

        if not product:

            return {
                "error": "Product not found"
            }

        #
        # Core Scoring Engines (100 Point Flip Score)
        #

        profit_result = self.profit.score(product)
        roi_result = self.roi.score(product)
        brand_result = self.brand.score(product)
        history_result = self.history.score(product_id, db)
        risk_result = self.risk.score(history_result)

        #
        # Future AI Insights
        #

        demand_result = self.demand.score(product)
        competition_result = self.competition.score(product)
        confidence_result = self.confidence.score(
            product,
            history_result
        )
        category_result = self.category.score(product)

        #
        # Final Flip Score
        #

        total_score = (

            profit_result["score"]

            + roi_result["score"]

            + brand_result["score"]

            + history_result["score"]

            + risk_result["score"]

        )

        #
        # Decision
        #

        if total_score >= 85:

            decision = "BUY NOW"

        elif total_score >= 70:

            decision = "CONSIDER"

        elif total_score >= 50:

            decision = "RESEARCH"

        else:

            decision = "PASS"

        #
        # Return (Backwards Compatible)
        #

        return {

            "product":
                product.name,

            "flip_score":
                total_score,

            "decision":
                decision,

            "breakdown":

                {

                    "profit_score":
                        profit_result["score"],

                    "roi_score":
                        roi_result["score"],

                    "brand_score":
                        brand_result["score"],

                    "history_score":
                        history_result["score"],

                    "risk_score":
                        risk_result["score"]

                },

            "metrics":

                {

                    "estimated_profit":
                        profit_result["details"]["estimated_profit"],

                    "estimated_roi":
                        roi_result["details"]["estimated_roi"]

                },

            #
            # New AI data (safe for frontend)
            #

            "ai_insights":

                {

                    "demand":
                        demand_result,

                    "competition":
                        competition_result,

                    "confidence":
                        confidence_result,

                    "category":
                        category_result

                },

            "recommendation":

                f"{decision}: {product.name} scored {total_score}/100"

        }