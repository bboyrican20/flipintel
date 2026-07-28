from sqlalchemy.orm import Session

from app.models.scan_history import ScanHistory


class HistoryEngine:
    """
    Calculates the scan history score.
    Maximum Score: 15
    """

    MAX_SCORE = 15

    def score(self, product_id: int, db: Session):

        history_count = (
            db.query(ScanHistory)
            .filter(
                ScanHistory.product_id == product_id
            )
            .count()
        )

        if history_count >= 10:
            score = 15

        elif history_count >= 5:
            score = 10

        elif history_count > 0:
            score = 5

        else:
            score = 0

        return {
            "name": "History",
            "score": score,
            "max_score": self.MAX_SCORE,
            "details": {
                "scan_count": history_count
            }
        }