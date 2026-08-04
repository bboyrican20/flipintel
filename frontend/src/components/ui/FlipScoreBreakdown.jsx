function FlipScoreBreakdown({ product }) {


    if (!product) {
        return null;
    }



    const buyPrice =
        Number(
            product.buy_price ??
            product.buyPrice ??
            0
        );



    const marketValue =
        Number(
            product.market_value ??
            product.market_price ??
            product.sell_price ??
            product.sellPrice ??
            0
        );



    const profit =
        Number(
            product.profit ??
            (marketValue - buyPrice)
        );



    const roi =
        buyPrice > 0
            ? Math.round((profit / buyPrice) * 100)
            : 0;



    const profitScore =
        profit > 150 ? 95 :
        profit > 75 ? 85 :
        70;



    const roiScore =
        roi > 200 ? 100 :
        roi > 100 ? 90 :
        75;



    const marketScore =
        marketValue > buyPrice * 2
            ? 92
            : 80;



    const sellSpeed =
        product.sell_speed === "FAST"
            ? 95
            : 85;



    return (

        <div className="flip-score-breakdown">


            <div className="flip-score-header">

                🔥 FlipIntel Score Breakdown

            </div>



            <p className="flip-score-subtitle">

                How FlipIntel calculated this opportunity

            </p>




            <div className="score-grid">



                <div className="score-item">

                    <span>
                        💰 Profit Potential
                    </span>

                    <strong>
                        {profitScore}/100
                    </strong>

                </div>




                <div className="score-item">

                    <span>
                        📈 ROI Strength
                    </span>

                    <strong>
                        {roiScore}/100
                    </strong>

                </div>




                <div className="score-item">

                    <span>
                        🌎 Market Advantage
                    </span>

                    <strong>
                        {marketScore}/100
                    </strong>

                </div>




                <div className="score-item">

                    <span>
                        ⚡ Sell Speed
                    </span>

                    <strong>
                        {sellSpeed}/100
                    </strong>

                </div>



            </div>



        </div>

    );

}


export default FlipScoreBreakdown;