import { useEffect, useState } from "react";
import axios from "axios";

import HotDealCard from "../components/ui/HotDealCard";


const API = "http://localhost:8000";


function Deals() {


    const [deals,setDeals] = useState([]);



    useEffect(()=>{


        async function loadDeals(){


            try{


                const response = await axios.get(
                    `${API}/dashboard/top-deals`
                );


                setDeals(
                    response.data.top_deals || []
                );


            }
            catch(error){


                console.error(
                    "Failed loading deals:",
                    error
                );


            }


        }


        loadDeals();


    },[]);





    return (


        <div className="deals-page">


            <header>


                <h1>
                    🔥 Hot Deals
                </h1>


                <p>
                    AI ranked flipping opportunities
                </p>


            </header>





            <div className="deals-grid">


                {
                deals.map((deal)=>(


                    <HotDealCard

                        key={deal.product_id}

                        product={deal}

                    />


                ))

                }


            </div>


        </div>


    );


}


export default Deals;