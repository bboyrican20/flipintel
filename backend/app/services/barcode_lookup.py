from typing import Optional


MOCK_PRODUCTS = {
    "885911406123": {
        "name": "DeWalt 20V Max Drill Kit",
        "brand": "DeWalt",
        "category": "Power Tools",
        "market_price": 179.00,
    },
    "045242637285": {
        "name": "Milwaukee M18 Fuel Combo Kit",
        "brand": "Milwaukee",
        "category": "Power Tools",
        "market_price": 499.00,
    },
    "088381234567": {
        "name": "Makita 18V LXT Combo Kit",
        "brand": "Makita",
        "category": "Power Tools",
        "market_price": 399.00,
    },
}


def lookup_barcode(barcode: str) -> Optional[dict]:
    """
    Temporary barcode lookup.

    Later this function will call real APIs like:
    - UPCitemDB
    - BarcodeLookup
    - eBay
    - Amazon
    """

    return MOCK_PRODUCTS.get(barcode)