import {
    useEffect,
    useState
} from "react";

import axios from "axios";


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

            <div className="deal-ai">


                🤖 Analyzing Deal...


            </div>

        );


    }







    return (


        <div className="deal-ai">



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








            <h4>

                Why FlipIntel Likes This

            </h4>





            {


            analysis.reasons &&

            analysis.reasons.map(

                (reason,index)=>(


                    <p key={index}>


                        ✅ {reason}


                    </p>


                )

            )


            }






        </div>


    );


}



export default DealAI;