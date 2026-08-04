function DealAI({ analysis }) {


    if(!analysis){

        return (

            <div className="deal-ai">

                🤖 Analyzing Deal...

            </div>

        );

    }




    return (


        <div className="deal-ai premium-verdict-card">



            <div className="verdict-header">


                <h3>

                    🤖 FlipIntel Verdict

                </h3>


            </div>






            <div className="verdict-grid">





                <div className="verdict-stat">


                    <span>

                        AI Confidence

                    </span>


                    <strong className="confidence-value">

                        {analysis.confidence}/100

                    </strong>


                </div>







                <div className="verdict-stat">


                    <span>

                        Risk

                    </span>


                    <strong className="risk-value">

                        {analysis.risk}

                    </strong>


                </div>







                <div className="verdict-stat">


                    <span>

                        Flip Window

                    </span>


                    <strong>

                        {analysis.flip_window}

                    </strong>


                </div>




            </div>








            <div className="recommendation-banner">



                <span className="recommendation-dot">

                    🟢

                </span>




                <strong>

                    {analysis.recommendation}

                </strong>



            </div>






        </div>


    );


}


export default DealAI;