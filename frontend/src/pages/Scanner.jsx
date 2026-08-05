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
import BarcodeScanner from "../components/ui/BarcodeScanner";


const API = "http://localhost:8000";


function Scanner() {


    const [barcode,setBarcode] = useState("");

    const [buyPrice,setBuyPrice] = useState("");

    const [retailer,setRetailer] = useState("");

    const [result,setResult] = useState(null);

    const [marketplace,setMarketplace] = useState(null);

    const [loading,setLoading] = useState(false);

    const [adding,setAdding] = useState(false);

    const [showCamera,setShowCamera] = useState(false);

    const [barcodeFound,setBarcodeFound] = useState(false);

const [productPreview,setProductPreview] = useState(null); 

    const retailers = [
    "Home Depot",
    "Lowe's",
    "Walmart",
    "Target",
    "Best Buy",
    "Amazon",
    "Costco",
    "Other"
];



async function lookupProduct(code){

    try{

        const response = await axios.get(

            `${API}/scanner/lookup/${code}`

        );


        if(response.data.found){

            setProductPreview(

                response.data.product

            );

        }


    }

    catch(error){

        console.error(

            "Product lookup error:",

            error

        );

    }

}





async function scanProduct(scannedBarcode = null){


        try{


            const activeBarcode = scannedBarcode || barcode;


            if(!activeBarcode){

                alert("Scan or enter a barcode first");

                return;

            }



            if(!buyPrice){

                alert("Enter purchase price first");

                return;

            }



            setLoading(true);



            const response = await axios.post(

                `${API}/scanner/barcode`,

                {

                    barcode: activeBarcode,

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





    function handleBarcodeScan(code){


    console.log(

        "Received barcode:",

        code

    );


    setBarcode(code);


    setBarcodeFound(true);


    setShowCamera(false);


    lookupProduct(code);



        if(buyPrice){


            setTimeout(()=>{


                scanProduct(code);


            },500);


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





        <button

            className="primary-button"

            onClick={()=>setShowCamera(!showCamera)}

        >

            📷

            {

                showCamera

                ?

                " Hide Camera"

                :

                " Scan With Camera"

            }

        </button>





        {

            showCamera &&

            <BarcodeScanner

                onScan={handleBarcodeScan}

                onClose={()=>setShowCamera(false)}

            />

        }





        {

            barcodeFound &&


            <div className="scanner-success">

                ✅ Barcode detected

            </div>

        }





        {

            productPreview &&


            <div className="scanner-box">


                <h3>

                    📦 Product Found

                </h3>


                <strong>

                    {productPreview.name}

                </strong>


                <p>

                    Brand:

                    {" "}

                    {productPreview.brand}

                </p>


                <p>

                    Category:

                    {" "}

                    {productPreview.category}

                </p>


                <p>

                    Market Value:

                    {" "}

                    ${productPreview.market_price}

                </p>


            </div>

        }





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





        <div className="quick-price-buttons">


            <button

                onClick={()=>setBuyPrice("25")}

            >

                $25

            </button>



            <button

                onClick={()=>setBuyPrice("50")}

            >

                $50

            </button>



            <button

                onClick={()=>setBuyPrice("100")}

            >

                $100

            </button>



            <button

                onClick={()=>setBuyPrice("150")}

            >

                $150

            </button>


        </div>





        <select

            value={retailer}

            onChange={(e)=>

                setRetailer(e.target.value)

            }

        >

            <option value="">

                Select Retailer

            </option>


            {

                retailers.map((store)=>(

                    <option

                        key={store}

                        value={store}

                    >

                        {store}

                    </option>

                ))

            }


        </select>





        <button

            className="primary-button"

            onClick={()=>scanProduct()}

            disabled={loading}

        >


            {

                loading

                ?

                "🤖 Analyzing AI Data..."

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