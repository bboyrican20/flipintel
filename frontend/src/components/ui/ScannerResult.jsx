import {
    PackagePlus,
    ShieldCheck,
    TrendingUp,
    Clock,
    Brain,
    Flame,
    BarChart3
} from "lucide-react";

import ProductImage from "./ProductImage";


function ScannerResult({
    result,
    addInventory,
    adding
}) {


    const confidence =
    result.confidence?.confidence
    ??
    0;


    const marketplace =
        result.marketplace_intelligence;


    const flipDecision =
    result.analysis?.recommendation
    ||
    result.decision?.action
    ||
    "RESEARCH";


    const risk =
        result.confidence?.risk ||
        result.decision?.risk ||
        "LOW";


    const roi =
    result.roi
    ??
    0;


    const profit =
    result.profit
    ??
    0;


    const maxBuyPrice =
        result.decision?.max_buy_price;



    return (

        <section className="ai-scanner-result">


            <div className="scanner-result-header">

                <span>
                    🤖 AI SCAN COMPLETE
                </span>


                <span className="confidence">

                    {confidence}% Confidence

                </span>

            </div>





            <div className="scanner-product">


                <ProductImage

                    image={result.image}

                    title={result.product}

                    brand={result.brand}

                />



                <div className="scanner-product-info">


                    <h2>
                        {result.product}
                    </h2>


                    <p className="category">

                        {result.brand}
                        {" • "}
                        {result.category}

                    </p>




                    <div className="scanner-metrics">


                        <div>

                            <span>
                                Market Value
                            </span>


                            <strong>

                                ${result.market_price?.toFixed(2)}

                            </strong>

                        </div>




                        <div>

                            <span>
                                Profit
                            </span>


                            <strong className="profit">

                                +${profit.toFixed(2)}

                            </strong>

                        </div>




                        <div>

                            <span>
                                ROI
                            </span>


                            <strong className="roi">

                                {roi.toFixed(2)}%

                            </strong>


                        </div>


                    </div>


                </div>


            </div>







            <div className="decision-engine">


                <h3>

                    🧠 FlipIntel Decision

                </h3>



                <div className="decision-grid">


                    <div>

                        <ShieldCheck size={18}/>

                        <span>
                            Decision
                        </span>


                        <strong>

                            {flipDecision}

                        </strong>


                    </div>





                    <div>

                        <TrendingUp size={18}/>

                        <span>
                            Confidence
                        </span>


                        <strong>

                            {confidence}%

                        </strong>

                    </div>





                    <div>

                        <Clock size={18}/>

                        <span>
                            Flip Window
                        </span>


                        <strong>

                            3–7 Days

                        </strong>

                    </div>





                    <div>

                        <span>
                            Risk
                        </span>


                        <strong>

                            {risk}

                        </strong>


                    </div>


                </div>


            </div>







            <div className="ai-breakdown-card">


                <h3>

                    <Brain size={20}/>

                    AI Deal Breakdown

                </h3>




                <div className="ai-breakdown-grid">


                    <div>

                        <BarChart3 size={18}/>

                        <span>
                            Profit Potential
                        </span>


                        <strong>
                            {profit >= 100 ? "HIGH" : "MEDIUM"}
                        </strong>

                    </div>




                    <div>

                        <Flame size={18}/>

                        <span>
                            Market Demand
                        </span>


                        <strong>

                            {
                                marketplace?.confidence >= 90
                                ?
                                "HIGH"
                                :
                                "MEDIUM"
                            }

                        </strong>

                    </div>




                    <div>

                        <span>
                            🏷️ Brand Strength
                        </span>


                        <strong>

                            {
                                result.brand
                                ?
                                "STRONG"
                                :
                                "UNKNOWN"
                            }

                        </strong>


                    </div>





                    <div>

                        <span>
                            📦 Resale Speed
                        </span>


                        <strong>
                            FAST
                        </strong>

                    </div>



                </div>






                {
                    maxBuyPrice &&

                    <div className="max-buy-price">

                        <span>
                            Maximum Buy Price
                        </span>


                        <strong>

                            ${maxBuyPrice.toFixed(2)}

                        </strong>

                    </div>

                }



            </div>







            <button

                className="buy-button"

                onClick={addInventory}

                disabled={adding}

            >

                <PackagePlus/>


                {
                    adding
                    ?
                    "Adding..."
                    :
                    "ADD TO INVENTORY"
                }


            </button>



        </section>


    );

}


export default ScannerResult;