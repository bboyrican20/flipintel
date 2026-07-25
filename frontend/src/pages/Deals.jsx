import { useEffect, useState } from "react";
import axios from "axios";


const API = "http://localhost:8000";



function Deals(){


const [deals,setDeals] = useState([]);



useEffect(()=>{


async function loadDeals(){


const response = await axios.get(
`${API}/deals/feed`
);


setDeals(
response.data.hot_deals || []
);


}


loadDeals();


},[]);






async function addInventory(deal){


try{


await axios.post(
`${API}/inventory/`,
{

product:
deal.product,


retailer:
deal.retailer,


purchase_price:
deal.buy_price,


expected_sale_price:
deal.market_price,


projected_profit:
deal.profit

}

);



alert(
"Added to Inventory ✅"
);



}catch(error){


console.error(
error
);


alert(
"Could not add item"
);


}


}






return (

<div className="deals-page">


<h1>

🔥 Hot Deals

</h1>



<p>

AI ranked flipping opportunities

</p>




<div className="deal-grid">


{deals.map(deal=>(


<div 
className="deal"
key={deal.product_id}
>


<div className="decision">

{deal.decision}

</div>



<h2>

{deal.product}

</h2>


<p>

🏪 {deal.retailer}

</p>



<h3>

Flip Score:
{deal.score}/100

</h3>



<p>

Buy:
${deal.buy_price}

</p>



<p>

Market:
${deal.market_price}

</p>



<p className="profit">

Profit:
+${deal.profit}

</p>



<p>

ROI:
{deal.roi}%

</p>




<button
onClick={() => addInventory(deal)}
>

📦 Add To Inventory

</button>



</div>


))}



</div>



</div>

);


}


export default Deals;