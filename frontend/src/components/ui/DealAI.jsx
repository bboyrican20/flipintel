import { useEffect, useState } from "react";
import axios from "axios";

const API = "http://localhost:8000";


function DealAI({ productId }) {


    const [analysis, setAnalysis] = useState(null);



    useEffect(() => {


        if (!productId) return;


        async function loadAI() {


            try {


                const response = await axios.get(

                    `${API}/deal-ai/${productId}`

                );


                setAnalysis(
                    response.data
                );


            }
            catch(error) {


                console.error(
                    "AI Analysis Error:",
                    error
                );


            }


        }


        loadAI();


    }, [productId]);





    if (!analysis) {


        return (

            <div className="deal-ai-card loading">

                🤖 Analyzing Deal...

            </div>

        );

    }





    return (

        <div className="deal-ai-card">



            <div className="deal-ai-header">


                <h3>
                    🤖 FlipIntel Verdict
                </h3>


            </div>





            <div className="ai-confidence">


                <span>
                    AI Confidence
                </span>


                <strong>
                    {analysis.confidence}/100
                </strong>


            </div>





            <div className="confidence-bar">


                <div

                    className="confidence-fill"

                    style={{
                        width: `${analysis.confidence}%`
                    }}

                />


            </div>





            <div className="ai-recommendation">


                🟢 {analysis.recommendation}


            </div>





            <div className="ai-details">


                <div>

                    <span>
                        Risk
                    </span>

                    <strong>
                        {analysis.risk}
                    </strong>

                </div>



                <div>

                    <span>
                        Flip Window
                    </span>

                    <strong>
                        {analysis.flip_window}
                    </strong>

                </div>


            </div>





            <div className="ai-reasons">


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



        </div>

    );

}


export default DealAI;