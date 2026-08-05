function ConfidenceMeter({ confidence }) {


    if (confidence === undefined || confidence === null) {

        return null;

    }




    let label = "LOW CONFIDENCE";


    if (confidence >= 90) {

        label = "VERY HIGH CONFIDENCE";

    }

    else if (confidence >= 75) {

        label = "HIGH CONFIDENCE";

    }

    else if (confidence >= 60) {

        label = "MODERATE CONFIDENCE";

    }






    return (


        <div className="confidence-meter-card">



            <div className="confidence-header">

                🧠 FlipIntel Confidence

            </div>





            <div className="confidence-score">

                {confidence}%

            </div>





            <div className="confidence-bar">


                <div

                    className="confidence-fill"

                    style={{

                        width: `${confidence}%`

                    }}

                />


            </div>







            <div className="confidence-label">

                {label}

            </div>







            <div className="confidence-factors">


                <div>

                    ✓ Profit Potential

                </div>


                <div>

                    ✓ ROI Strength

                </div>


                <div>

                    ✓ Market Advantage

                </div>


                <div>

                    ✓ Sales Velocity

                </div>


            </div>





        </div>


    );

}


export default ConfidenceMeter;