function ScannerFlipScore({ score }) {


    const value = score ?? 0;


    return (

        <div className="scanner-flip-score">


            <div className="flip-score-title">

                🔥 FLIP SCORE

            </div>



            <div className="flip-score-number">

                {value}

            </div>



            <div className="flip-score-max">

                /100

            </div>


        </div>

    );

}


export default ScannerFlipScore;