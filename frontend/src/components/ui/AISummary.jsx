function AISummary({ summary }) {


    if (!summary) {

        return null;

    }



    return (

        <div className="ai-summary-card">


            <div className="ai-summary-header">

                🤖 FlipIntel AI Summary

            </div>




            <p>

                {summary}

            </p>



        </div>

    );

}


export default AISummary;