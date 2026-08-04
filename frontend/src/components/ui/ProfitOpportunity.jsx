function ProfitOpportunity({ product }) {


    const buyPrice = Number(product.buy_price || 0);


    const marketPrice =
        Number(product.market_price) ||
        Number(product.expected_sale) ||
        179;



    const profit =
        Number(product.profit) ||
        (marketPrice - buyPrice);



    const percentage = marketPrice > 0

        ? Math.round((buyPrice / marketPrice) * 100)

        : 0;



    const upside = buyPrice > 0

        ? Math.round(((marketPrice - buyPrice) / buyPrice) * 100)

        : 0;



    return (

        <div className="profit-opportunity premium-opportunity-card">



            <div className="opportunity-header">


                <div className="ai-badge">

                    💰

                </div>


                <div>

                    <h3>

                        Profit Opportunity

                    </h3>


                    <p>

                        AI market valuation analysis

                    </p>

                </div>


            </div>





            <div className="price-row">



                <div className="price-box cost">


                    <span>

                        YOUR COST

                    </span>


                    <strong>

                        ${buyPrice}

                    </strong>


                </div>





                <div className="arrow">

                    ➜

                </div>





                <div className="price-box market">


                    <span>

                        MARKET VALUE

                    </span>


                    <strong>

                        ${marketPrice}

                    </strong>


                </div>



            </div>







            <div className="profit-banner">


                <span>

                    🔥 Your Edge

                </span>


                <strong>

                    +${profit}

                </strong>


            </div>







            <div className="valuation-card">

    <div className="valuation-text">

        You are acquiring this product at

        <strong>
            {" "}{percentage}%
        </strong>

        of estimated market value.

    </div>


    <div className="upside-highlight">

        <span>
            🚀 Upside Potential
        </span>

        <strong>
            {upside}%
        </strong>

    </div>


</div>



<div className="signal-card">

    <span>
        📈 Market Signal
    </span>


    <strong className="positive">

        STRONG BUY

    </strong>


</div>





        </div>

    );

}


export default ProfitOpportunity;