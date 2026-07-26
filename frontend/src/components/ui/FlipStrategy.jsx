import { useEffect, useState } from "react";
import axios from "axios";


const API = "http://localhost:8000";



function FlipStrategy({ productId }) {


    const [strategy, setStrategy] = useState(null);



    useEffect(() => {


        if (!productId) return;



        async function loadStrategy() {


            try {


                const response = await axios.get(

                    `${API}/flip-strategy/${productId}`

                );


                setStrategy(

                    response.data.strategy

                );


            }
            catch(error) {


                console.error(

                    "Flip Strategy Error:",

                    error

                );


            }


        }



        loadStrategy();



    }, [productId]);





    if (!strategy) {


        return null;


    }





    return (

        <div className="flip-strategy-card">


            <h3>
                💡 Flip Strategy
            </h3>



            <div className="strategy-grid">


                <div>

                    <span>
                        Buy Price
                    </span>

                    <strong>
                        ${strategy.buy_price}
                    </strong>

                </div>



                <div>

                    <span>
                        Target Sale
                    </span>

                    <strong>
                        ${strategy.target_sale_price}
                    </strong>

                </div>



                <div>

                    <span>
                        Recommended Listing
                    </span>

                    <strong>
                        ${strategy.recommended_listing}
                    </strong>

                </div>



                <div>

                    <span>
                        Minimum Offer
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