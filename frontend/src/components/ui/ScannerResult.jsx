import {
    Search,
    PackagePlus
} from "lucide-react";


function ScannerResult({
    result,
    addInventory,
    adding
}) {


    return (

        <section className="ai-scanner-result">


            <div className="scanner-result-header">

                <span>
                    🤖 AI SCAN COMPLETE
                </span>


                <span className="confidence">

                    {result.roi > 100
                        ? "94%"
                        : "78%"
                    } Confidence

                </span>

            </div>




            <h2>

                {result.product}

            </h2>




            <p className="category">

                {result.brand} • {result.category}

            </p>





            <div className="scanner-metrics">


                <div>

                    <span>
                        Market Value
                    </span>

                    <strong>
                        ${result.market_price}
                    </strong>

                </div>




                <div>

                    <span>
                        Profit
                    </span>

                    <strong className="profit">

                        +${result.profit}

                    </strong>

                </div>




                <div>

                    <span>
                        ROI
                    </span>

                    <strong className="roi">

                        {result.roi.toFixed(2)}%

                    </strong>

                </div>


            </div>






            <div className="ai-recommendation">


                <h3>

                    {result.analysis?.recommendation}

                </h3>


                <p>

                    {result.deal_explanation?.summary}

                </p>


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