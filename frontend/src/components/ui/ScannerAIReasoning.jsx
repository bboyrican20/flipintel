function ScannerAIReasoning({ reasoning }) {


    if (!reasoning || reasoning.length === 0) {

        return null;

    }



    return (


        <div className="scanner-ai-reasoning">



            <div className="scanner-ai-title">

                🧠 Why FlipIntel Recommends This

            </div>





            <div className="scanner-ai-list">


                {reasoning.map((item,index)=>(


                    <div

                        key={index}

                        className="scanner-ai-item"

                    >

                        ✅ {item}

                    </div>


                ))}



            </div>




        </div>


    );


}


export default ScannerAIReasoning;