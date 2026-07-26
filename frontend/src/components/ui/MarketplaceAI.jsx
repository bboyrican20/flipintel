import {
    useEffect,
    useState
} from "react";

import axios from "axios";


const API = "http://localhost:8000";



function MarketplaceAI({productId}) {


    const [marketplace,setMarketplace] = useState(null);



    useEffect(()=>{


        async function loadMarketplace(){


            try{


                const response = await axios.get(

                    `${API}/marketplace/${productId}`

                );


                setMarketplace(
                    response.data.marketplace
                );


            }
            catch(error){

                console.error(
                    "Marketplace AI Error:",
                    error
                );

            }


        }



        if(productId){

            loadMarketplace();

        }


    },[productId]);





    if(!marketplace){

        return (

            <div className="marketplace-ai">

                🌎 Analyzing Marketplace...

            </div>

        );

    }





    return (

        <div className="marketplace-ai">


            <h3>
                🌎 Best Marketplace
            </h3>



            <h2>
                🥇 {marketplace.best_marketplace}
            </h2>



            <div className="marketplace-row">

                💰 Expected Sale:

                <strong>
                    ${marketplace.expected_sale_price}
                </strong>

            </div>



            <div className="marketplace-row">

                ⚡ Sell Speed:

                <strong>
                    {marketplace.sell_speed}
                </strong>

            </div>



            <div className="marketplace-row">

                🎯 Confidence:

                <strong>
                    {marketplace.confidence}/100
                </strong>

            </div>


        </div>

    );


}


export default MarketplaceAI;