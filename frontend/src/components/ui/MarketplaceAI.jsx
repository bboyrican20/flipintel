function MarketplaceAI({ marketplace }) {


    if (!marketplace) {

        return null;

    }


    const sources = marketplace.sources || {};


    const bestMarketplace = Object.entries(sources).length

        ? Object.entries(sources)
            .reduce((a,b)=> a[1] > b[1] ? a : b)[0]

        : "N/A";



    return (

        <div className="marketplace-ai">


            <div className="marketplace-title">

                🌎 Marketplace Intelligence

            </div>



            <div className="marketplace-best">


                🏆 Best Selling Channel


                <strong>

                    {
                        bestMarketplace
                            .charAt(0)
                            .toUpperCase()
                        +
                        bestMarketplace.slice(1)

                    }

                </strong>


            </div>





            <div className="marketplace-prices">


                <div>

                    🛒 eBay

                    <strong>

                        ${sources.ebay?.toFixed(2)}

                    </strong>

                </div>



                <div>

                    📦 Amazon

                    <strong>

                        ${sources.amazon?.toFixed(2)}

                    </strong>

                </div>



                <div>

                    🏪 Facebook

                    <strong>

                        ${sources.facebook?.toFixed(2)}

                    </strong>

                </div>


            </div>





            <div className="marketplace-stats">


                <div>

                    <span>
                        📊 AI Average
                    </span>

                    <strong>
                        ${marketplace.market_price?.toFixed(2)}
                    </strong>

                </div>



                <div>

                    <span>
                        📈 Spread
                    </span>

                    <strong>
                        ${marketplace.spread?.toFixed(2)}
                    </strong>

                </div>



                <div>

                    <span>
                        🤖 Confidence
                    </span>

                    <strong>
                        {marketplace.confidence}%
                    </strong>

                </div>


            </div>


        </div>

    );

}


export default MarketplaceAI;