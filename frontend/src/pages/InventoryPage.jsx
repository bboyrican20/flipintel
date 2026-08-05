import { useEffect, useState } from "react";
import axios from "axios";

import {
    Package,
    DollarSign,
    TrendingUp,
    CheckCircle,
    ShoppingBag
} from "lucide-react";


const API = "http://localhost:8000";


function InventoryPage(){


    const [inventory,setInventory] = useState([]);

    const [showHistory,setShowHistory] = useState(false);




    async function sellItem(item){

        try{

            const salePrice = prompt(
                "Enter sale price:",
                item.expected_sale_price
            );


            if(!salePrice){
                return;
            }


            await axios.post(

                `${API}/sales/${item.inventory_id}`,

                {
                    sale_price:Number(salePrice)
                }

            );


            alert(
                "Item marked as sold!"
            );


            window.location.reload();


        }
        catch(error){

            console.error(
                "Sell error:",
                error
            );


            alert(
                "Failed selling item"
            );

        }

    }






    useEffect(()=>{


        async function loadInventory(){


            try{


                const response = await axios.get(

                    `${API}/inventory/`

                );


                setInventory(

                    response.data.inventory || []

                );


            }
            catch(error){

                console.error(
                    "Inventory error:",
                    error
                );

            }


        }


        loadInventory();


    },[]);








    const products = inventory.map(item=>({

        ...item,

        inventory_id:item.inventory_id,

        status:item.status,

        retailer:item.retailer,

        purchase_price:item.purchase_price,

        expected_sale_price:item.expected_sale_price,

        projected_profit:item.projected_profit

    }));







    const activeProducts = products.filter(

        item => item.status !== "SOLD"

    );



    const soldProducts = products.filter(

        item => item.status === "SOLD"

    );







    const inventoryValue = activeProducts.reduce(

        (sum,item)=>

            sum + Number(item.expected_sale_price || 0),

        0

    );






    const profit = activeProducts.reduce(

        (sum,item)=>

            sum + Number(item.projected_profit || 0),

        0

    );







    return (

        <div className="inventory-page">


            <header>

                <h1>

                    📦 Inventory Command Center

                </h1>


                <p>

                    Track every flip from purchase to profit

                </p>


            </header>








            <section className="stats-grid">


                <div className="stat-card">

                    <Package/>

                    <h3>
                        Active Listings
                    </h3>

                    <strong>
                        {activeProducts.length}
                    </strong>

                </div>





                <div className="stat-card">

                    <CheckCircle/>

                    <h3>
                        Sold Items
                    </h3>

                    <strong>
                        {soldProducts.length}
                    </strong>

                </div>





                <div className="stat-card">

                    <DollarSign/>

                    <h3>
                        Inventory Value
                    </h3>

                    <strong>
                        ${inventoryValue}
                    </strong>

                </div>





                <div className="stat-card">

                    <TrendingUp/>

                    <h3>
                        Projected Profit
                    </h3>

                    <strong className="profit">

                        +${profit}

                    </strong>

                </div>


            </section>










            <h2>

                📦 Active Inventory

            </h2>





            <div className="inventory-grid">


            {

                activeProducts.map(item=>(


                    <div

                        className="inventory-card"

                        key={item.inventory_id}

                    >


                        <div className="inventory-status">

                            🟢 ACTIVE

                        </div>




                        <h2>

                            {item.product || item.name}

                        </h2>




                        <p>

                            🏪 {item.retailer || "Unknown"}

                        </p>





                        <div className="inventory-row">

                            <span>
                                Bought
                            </span>

                            <strong>
                                ${item.purchase_price}
                            </strong>

                        </div>





                        <div className="inventory-row">

                            <span>
                                Expected Sale
                            </span>

                            <strong>
                                ${item.expected_sale_price}
                            </strong>

                        </div>





                        <div className="inventory-row">

                            <span>
                                Profit
                            </span>

                            <strong className="profit">

                                +${item.projected_profit}

                            </strong>

                        </div>





                        <button

                            className="buy-button"

                            onClick={()=>sellItem(item)}

                        >

                            <ShoppingBag/>

                            Mark Sold


                        </button>


                    </div>


                ))

            }


            </div>









            <button

                className="primary-button"

                onClick={()=>setShowHistory(!showHistory)}

            >

                🏆

                {

                    showHistory

                    ? 

                    " Hide Flip History"

                    :

                    ` View Flip History (${soldProducts.length})`

                }


            </button>









            {

                showHistory &&


                <section>


                    <h2>

                        🏆 Flip History

                    </h2>



                    <div className="inventory-grid">


                    {

                        soldProducts.map(item=>(


                            <div

                                className="inventory-card"

                                key={item.inventory_id}

                            >


                                <div className="inventory-status">

                                    💰 SOLD

                                </div>




                                <h2>

                                    {item.product || item.name}

                                </h2>




                                <p>

                                    🏪 {item.retailer || "Unknown"}

                                </p>





                                <div className="inventory-row">

                                    <span>
                                        Bought
                                    </span>

                                    <strong>
                                        ${item.purchase_price}
                                    </strong>

                                </div>





                                <div className="inventory-row">

                                    <span>
                                        Sold For
                                    </span>

                                    <strong>

                                        ${item.sale_price || item.expected_sale_price}

                                    </strong>

                                </div>





                                <div className="inventory-row">

                                    <span>
                                        Profit
                                    </span>

                                    <strong className="profit">

                                        +${item.actual_profit || item.projected_profit}

                                    </strong>

                                </div>


                            </div>


                        ))

                    }


                    </div>


                </section>


            }


        </div>

    );


}


export default InventoryPage;