import { useEffect, useState } from "react";
import axios from "axios";

import FlipStrategy from "./FlipStrategy";


const API = "http://localhost:8000";



function DealAI({ productId }) {


    const [analysis,setAnalysis] = useState(null);



    useEffect(()=>{


        async function loadAI(){


            try{


                console.log(
                    "AI Product ID:",
                    productId
                );


                const response = await axios.get(

    `${API}/deal-ai/${productId}`

);


console.log(
    "DEAL AI RESPONSE:",
    response.data
);


                setAnalysis(
                    response.data
                );


            }
            catch(error){


                console.error(

                    "AI Loading Error:",

                    error

                );


            }


        }



        if(productId){

            loadAI();

        }



    },[productId]);





    if(!analysis){


        return (

            <div className="deal-ai-card">

                🤖 Analyzing Deal...

            </div>

        );


    }





    return (

        <div className="deal-ai-card">


            <h3>

                🤖 FlipIntel Verdict

            </h3>





            <div>


                AI Confidence:


                <strong>

                    {analysis.confidence}/100

                </strong>


            </div>





            <h2>

                🟢 {analysis.recommendation}

            </h2>





            <div>


                Risk:


                <strong>

                    {analysis.risk}

                </strong>


            </div>





            <div>


                Flip Window:


                <strong>

                    {analysis.flip_window}

                </strong>


            </div>





            <div>


                <h4>

                    Why FlipIntel Likes This

                </h4>



                {

                analysis.reasons?.map(

                    (reason,index)=>(


                        <p key={index}>

                            ✅ {reason}

                        </p>


                    )

                )

                }


            </div>





            <FlipStrategy

                productId={productId}

            />



        </div>

    );


}



export default DealAI;