import {
    useState
} from "react";

import axios from "axios";

import {
    ScanLine,
    Activity,
    Zap,
    TrendingUp
} from "lucide-react";

import ScannerResult from "../components/ui/ScannerResult";
import MarketplaceAI from "../components/ui/MarketplaceAI";


const API = "http://localhost:8000";


function Scanner() {


    const [barcode,setBarcode] = useState("");

    const [buyPrice,setBuyPrice] = useState("");

    const [retailer,setRetailer] = useState("");

    const [result,setResult] = useState(null);

    const [marketplace,setMarketplace] = useState(null);

    const [loading,setLoading] = useState(false);

    const [adding,setAdding] = useState(false);





    async function scanProduct(){


        try{


            setLoading(true);



            const response = await axios.post(

                `${API}/scanner/barcode`,

                {

                    barcode,

                    buy_price:Number(buyPrice),

                    retailer

                }

            );



            setResult(response.data);


            setMarketplace(
                response.data.marketplace_intelligence
            );


        }

        catch(error){


            console.error(
                "Scanner error:",
                error
            );


            alert(
                "Product scan failed"
            );


        }

        finally{


            setLoading(false);


        }


    }








    async function addInventory(){


        try{


            setAdding(true);



            await axios.post(

                `${API}/inventory/`,

                {

                    product_id:
                        result.product_id,


                    product:
                        result.product,


                    retailer,


                    purchase_price:
                        Number(buyPrice),


                    expected_sale_price:
                        result.market_price,


                    projected_profit:
                        result.profit

                }

            );



            alert(
                "Added to Inventory!"
            );


        }

        catch(error){


            console.error(

                "Inventory error:",
                error

            );


            alert(
                "Failed adding inventory"
            );


        }

        finally{


            setAdding(false);


        }


    }









    return (

        <div className="scanner-page">



            <header>


                <h1>
                    🤖 FlipIntel Scanner
                </h1>


                <p>
                    Real-time product intelligence engine
                </p>


            </header>








            <section className="scanner-box">


                <h2>

                    <ScanLine />

                    Scan Product

                </h2>





                <input

                    placeholder="Barcode"

                    value={barcode}

                    onChange={(e)=>

                        setBarcode(e.target.value)

                    }

                />






                <input

                    placeholder="Purchase Price"

                    value={buyPrice}

                    onChange={(e)=>

                        setBuyPrice(e.target.value)

                    }

                />






                <input

                    placeholder="Retailer"

                    value={retailer}

                    onChange={(e)=>

                        setRetailer(e.target.value)

                    }

                />







                <button

                    className="primary-button"

                    onClick={scanProduct}

                    disabled={loading}

                >

                    {

                        loading

                        ?

                        "Analyzing AI Data..."

                        :

                        "🚀 Analyze Product"

                    }


                </button>



            </section>









            {

                result &&

                <>


                    <ScannerResult

                        result={result}

                        addInventory={addInventory}

                        adding={adding}

                    />



                    <MarketplaceAI

                        marketplace={marketplace}

                    />


                </>


            }









            {

                result &&


                <section className="scanner-grid">



                    <div className="scanner-box">


                        <TrendingUp />


                        <h3>

                            Historical Performance

                        </h3>


                        <strong>

                            {

                                result.product_memory?.times_seen

                                ||

                                0

                            }

                            {" "}

                            Scans

                        </strong>


                    </div>








                    <div className="scanner-box">


                        <Activity />


                        <h3>

                            Average ROI

                        </h3>


                        <strong>

                            {

                                result.product_memory?.average_roi

                                ?

                                `${result.product_memory.average_roi.toFixed(1)}%`

                                :

                                "N/A"

                            }


                        </strong>


                    </div>








                    <div className="scanner-box">


                        <Zap />


                        <h3>

                            Buy Zone

                        </h3>


                        <strong>

                            {

                                result.product_memory?.buy_zone

                                ||

                                "UNKNOWN"

                            }


                        </strong>


                    </div>



                </section>


            }





        </div>

    );


}


export default Scanner;