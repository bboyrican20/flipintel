from app.services.flip_score_engine import FlipScoreEngine
from app.services.buy_price_engine import BuyPriceEngine
from app.services.decision_engine import DecisionEngine


class ScannerIntelligence:


    def __init__(self):

        self.flip_engine = FlipScoreEngine()

        self.buy_engine = BuyPriceEngine()

        self.decision_engine = DecisionEngine()



    def analyze(
        self,
        product,
        db,
        confidence,
        historical,
        analysis
    ):


        #
        # FLIP SCORE
        #

        flip_score = (
            self.flip_engine.calculate_score(
                product.id,
                db
            )
        )


        #
        # BUY PRICE
        #

        buy_price = (
            self.buy_engine.calculate(
                product.id,
                db
            )
        )


        #
        # DECISION ENGINE
        #

        decision = (
            self.decision_engine.decide(
                product,
                analysis,
                confidence,
                historical
            )
        )


        return {


            "product":
                product.name,


            "flip_score":

                flip_score,


            "buy_price_analysis":

                buy_price,


            "final_decision":

                decision

        }



scanner_intelligence = ScannerIntelligence()