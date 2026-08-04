function AIReasoning({ product }) {


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
            product.marketPrice ??
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
        Number(
            product.roi ??
            (
                buyPrice > 0
                    ? (profit / buyPrice) * 100
                    : 0
            )
        );



    const discount =
        marketValue > 0
            ? Math.round(
                ((marketValue - buyPrice) / marketValue) * 100
            )
            : 0;



    const brand =
        product.brand ??
        product.manufacturer ??
        "This brand";



    const category =
        product.category ??
        "product category";



    const sellSpeed =
        product.sell_speed ??
        "FAST";



    return (


        <div className="ai-reasoning-card">



            <div className="ai-reasoning-header">

                🧠 Why FlipIntel Picked This

            </div>




            <p className="ai-reasoning-subtitle">

                AI reasoning behind this opportunity

            </p>





            <div className="reasoning-list">



                <div className="reasoning-item">

                    ✅ Bought {discount}% below estimated market value

                </div>





                <div className="reasoning-item">

                    ✅ Projected profit opportunity of +${profit.toFixed(2)}

                </div>





                <div className="reasoning-item">

                    ✅ ROI potential of {roi.toFixed(2)}% exceeds FlipIntel targets

                </div>





                <div className="reasoning-item">

                    ✅ {brand} {category} products show {sellSpeed.toLowerCase()} resale potential

                </div>



            </div>


        </div>


    );

}


export default AIReasoning;