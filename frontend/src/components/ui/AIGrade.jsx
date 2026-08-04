function AIGrade({ grade }) {


    if (!grade) {

        return null;

    }



    return (

        <div className="ai-grade-card">


            <div className="ai-grade-header">

                🏆 FlipIntel Grade

            </div>




            <div className="grade-content">


                <div className="grade-letter">

                    {grade.letter}

                </div>



                <div className="grade-info">


                    <strong>

                        {grade.title}

                    </strong>


                    <p>

                        {grade.reason}

                    </p>


                </div>


            </div>


        </div>

    );

}


export default AIGrade;