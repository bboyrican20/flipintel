function FlipStrategy({ strategy }) {


    if (!strategy) {

        return null;

    }



    return (

        <div className="flip-strategy-card">





            <h3>

                🚀 Seller Action Plan

            </h3>







            <div className="strategy-grid">





                <div>


                    <span>

                        BUY AT

                    </span>


                    <strong>

                        ${strategy.buy_price}

                    </strong>


                </div>







                <div>


                    <span>

                        TARGET SALE

                    </span>


                    <strong>

                        ${strategy.target_sale_price}

                    </strong>


                </div>







                <div>


                    <span>

                        RECOMMENDED LISTING

                    </span>


                    <strong>

                        ${strategy.recommended_listing}

                    </strong>


                </div>







                <div>


                    <span>

                        ACCEPT OFFER

                    </span>


                    <strong>

                        ${strategy.minimum_offer}

                    </strong>


                </div>





            </div>









            <div className="strategy-profit">


                Expected Profit:


                <strong>

                    +${strategy.expected_profit}

                </strong>



            </div>









            <div className="strategy-advice">


                🧠


                {strategy.strategy}



            </div>







        </div>

    );

}


export default FlipStrategy;