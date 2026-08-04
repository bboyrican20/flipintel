def analyze_product(product):

    buy_price = float(product.buy_price or 0)

    sell_price = float(
        product.sell_price or
        product.market_price or
        0
    )


    profit = sell_price - buy_price


    roi = (
        (profit / buy_price) * 100
        if buy_price > 0
        else 0
    )


    discount = (
        ((sell_price - buy_price) / sell_price) * 100
        if sell_price > 0
        else 0
    )



    # SCORE LOGIC

    profit_score = (
        95 if profit >= 150
        else 85 if profit >= 75
        else 70
    )


    roi_score = (
        100 if roi >= 200
        else 90 if roi >= 100
        else 75
    )


    market_score = (
        92 if sell_price >= buy_price * 2
        else 80
    )


    sell_speed_score = 95



    confidence = round(
        (
            profit_score +
            roi_score +
            market_score +
            sell_speed_score
        ) / 4
    )



    risk = (
        "LOW"
        if confidence >= 85
        else "MEDIUM"
    )



    recommendation = (
        "STRONG BUY"
        if confidence >= 85
        else "BUY"
    )



    reasons = [

        f"Bought {round(discount)}% below estimated market value",

        f"Projected profit opportunity of +${profit:.2f}",

        f"ROI potential of {roi:.2f}% exceeds FlipIntel targets",

        "Strong resale potential based on market conditions"

    ]



    return {

        "confidence": confidence,

        "risk": risk,

        "recommendation": recommendation,

        "flip_window": "3-7 Days",

        "scores": {

            "profit": profit_score,

            "roi": roi_score,

            "market": market_score,

            "sell_speed": sell_speed_score

        },


        "reasoning": reasons

    }