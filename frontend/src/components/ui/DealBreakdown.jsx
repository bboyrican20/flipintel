function DealBreakdown({ product }) {


    const roi = product.roi || 0;

    const profit = product.profit || 0;



    let profitScore = 50;

    let demandScore = 70;

    let risk = "MEDIUM";

    let speed = "NORMAL";





    if (roi >= 100) {

        profitScore = 95;

    } 
    else if (roi >= 50) {

        profitScore = 80;

    }





    if (profit >= 75) {

        demandScore = 90;

    }





    if (roi >= 100 && profit >= 75) {

        risk = "LOW";

        speed = "FAST";

    }







    return (


        <div className="deal-breakdown premium-card">





            <div className="breakdown-title">



                <div className="ai-icon">

                    🧠

                </div>





                <div>


                    <h3>

                        Market Intelligence

                    </h3>





                    <p>

                        AI signals behind this opportunity

                    </p>



                </div>



            </div>









            <div className="breakdown-item">





                <div className="breakdown-header">



                    <span>

                        💰 Profit Potential

                    </span>





                    <strong>

                        {profitScore}%

                    </strong>



                </div>







                <div className="progress">


                    <div

                        className="progress-fill"

                        style={{

                            width:`${profitScore}%`

                        }}

                    />



                </div>





            </div>









            <div className="breakdown-item">





                <div className="breakdown-header">



                    <span>

                        📈 Market Demand

                    </span>





                    <strong>

                        {demandScore}%

                    </strong>



                </div>







                <div className="progress">


                    <div

                        className="progress-fill"

                        style={{

                            width:`${demandScore}%`

                        }}

                    />



                </div>





            </div>









            <div className="insight-grid">





                <div className="insight-box">



                    <span>

                        🛡️ Risk

                    </span>





                    <strong className={risk === "LOW" ? "positive" : ""}>

                        {risk}

                    </strong>



                </div>









                <div className="insight-box">



                    <span>

                        ⚡ Sell Speed

                    </span>





                    <strong>

                        {speed}

                    </strong>



                </div>





            </div>







        </div>


    );


}



export default DealBreakdown;