function RiskAnalysis({ riskAnalysis }) {


    if (!riskAnalysis) {

        return null;

    }



    return (

        <div className="risk-analysis-card">


            <div className="risk-header">

                ⚠️ FlipIntel Risk Analysis

            </div>





            <div className="risk-level">


                <span>

                    Risk Level

                </span>


                <strong>

                    {riskAnalysis.level}

                </strong>


            </div>







            <div className="risk-warnings">


                {
                    riskAnalysis.warnings?.map(

                        (warning, index) => (


                            <div

                                className="risk-item"

                                key={index}

                            >

                                ⚠️ {warning}

                            </div>


                        )

                    )
                }


            </div>



        </div>

    );

}


export default RiskAnalysis;