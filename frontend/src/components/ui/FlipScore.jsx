function FlipScore({ score }) {


    return (

        <div className="flip-score">





            <div className="score-label">


                🔥 FLIP SCORE


            </div>







            <div className="score-circle">



                <strong>

                    {score || 0}

                </strong>


                <span>

                    /100

                </span>



            </div>






        </div>

    );

}


export default FlipScore;