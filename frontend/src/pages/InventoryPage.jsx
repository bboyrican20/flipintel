import { useEffect, useState } from "react";
import axios from "axios";

import {
  Package,
  DollarSign,
  TrendingUp,
  CheckCircle
} from "lucide-react";


const API = "http://localhost:8000";


function InventoryPage(){


const [inventory,setInventory] = useState([]);



async function sellItem(item){

  try{


    const salePrice = prompt(
      "Enter sale price:",
      item.market_price
    );



    if(!salePrice){

      return;

    }



    await axios.post(

      `${API}/inventory/${item.inventory_id}/sell`,

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
      "Failed to sell item"
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






const products = inventory.map(

(item)=>({

...item.product,

inventory_id:item.inventory_id

})

);







const totalInvested = products.reduce(

(sum,item)=>

sum + Number(item.buy_price || item.purchase_price || 0),

0

);





const totalValue = products.reduce(

(sum,item)=>

sum + Number(item.market_price || item.expected_sale_price || 0),

0

);





const totalProfit = products.reduce(

(sum,item)=>

sum + Number(item.profit || item.projected_profit || 0),

0

);







return (

<div className="inventory-page">



<header>

<h1>

📦 Inventory Intelligence

</h1>


<p>

Track every flip from purchase to profit

</p>


</header>







<section className="stats">


<div className="card">

<Package/>

<h3>

Items Owned

</h3>


<strong>

{products.length}

</strong>


</div>






<div className="card">

<DollarSign/>

<h3>

Capital Invested

</h3>


<strong>

${totalInvested}

</strong>


</div>







<div className="card">

<TrendingUp/>

<h3>

Inventory Value

</h3>


<strong>

${totalValue}

</strong>


</div>







<div className="card">

<CheckCircle/>

<h3>

Potential Profit

</h3>


<strong className="profit">

+${totalProfit}

</strong>


</div>


</section>








<h2>

Current Inventory

</h2>







<div className="inventory-grid">



{

products.map((item)=>(


<div

className="inventory-card"

key={item.inventory_id}

>




<div className="status-badge">


{

item.status === "SOLD"

?

"💰 SOLD"

:

"🟢 AVAILABLE"

}


</div>







<h2>

{item.name}

</h2>







<p>

🏪 {item.retailer || "Unknown Retailer"}

</p>






<p>

🏷️ {item.brand || "Unknown Brand"}

</p>






<p>

📦 Sales Velocity:

{item.sales_velocity || "N/A"}

</p>








<div className="inventory-row">

<span>

Purchase

</span>


<strong>

${item.buy_price}

</strong>


</div>








<div className="inventory-row">

<span>

Market Value

</span>


<strong>

${item.market_price}

</strong>


</div>








<div className="inventory-row">

<span>

Profit

</span>


<strong className="profit">

+${item.profit}

</strong>


</div>








<div className="inventory-row">

<span>

ROI

</span>


<strong>

{item.roi?.toFixed(0)}%

</strong>


</div>








<button

onClick={() => sellItem(item)}

>

Mark Sold

</button>





</div>


))


}



</div>





</div>

);


}


export default InventoryPage;