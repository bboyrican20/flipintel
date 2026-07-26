import ROIBadge from "./ROIBadge";
import DealAI from "./DealAI";


function HotDealCard({ product, onBuy }) {


    return (

        <div className="hot-deal-card">


            <div className="deal-header">


                <span className="deal-fire">
                    🔥 HOT DEAL
                </span>


                <ROIBadge
                    roi={product.roi}
                />


            </div>


            <h2>
                {product.product}
            </h2>


            <p className="retailer">
                🏪 {product.retailer || "Retailer"}
            </p>


            <div className="deal-score">

                AI Deal Score:

                <strong>
                    {" "}
                    {product.deal_score || product.flipintel_score || 0}/100
                </strong>

            </div>



            <div className="deal-prices">


                <div>

                    <span>
                        Profit
                    </span>


                    <strong className="profit">

                        +${product.profit || 0}

                    </strong>

                </div>



                <div>

                    <span>
                        ROI
                    </span>


                    <strong>

                        {product.roi || 0}%

                    </strong>

                </div>


            </div>



            <div className="recommendation">

                {product.recommendation}

            </div>



            <DealAI

                productId={product.product_id}

            />



            <button

                className="buy-button"

                onClick={onBuy}

            >

                🛒 BUY NOW

            </button>


        </div>

    );

}


export default HotDealCard;