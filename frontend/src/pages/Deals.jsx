import { useEffect, useState } from "react";
import axios from "axios";

import {
  Flame,
  TrendingUp,
  DollarSign,
  ShieldCheck,
  Clock
} from "lucide-react";


const API = "http://localhost:8000";



function Deals(){


const [deals,setDeals] = useState([]);




useEffect(()=>{


async function loadDeals(){


try{


const response = await axios.get(
`${API}/deals/feed`
);


setDeals(
response.data.hot_deals || []
);



}catch(error){


console.error(
"Deals error:",
error
);


}


}


loadDeals();


},[]);







return (

<div className="deals-page">


<header>

<h1>

<Flame/>

Hot Deals

</h1>


<p>

AI powered flipping opportunities

</p>


</header>






<div className="deals-grid">



{deals.map((deal)=>(



<div 
className="deal-card"
key={deal.product_id}
>




<div className="deal-top">


<span className="buy-badge">

{deal.decision}

</span>


<span className="score-badge">

{deal.score}/100

</span>


</div>





<h2>

{deal.product}

</h2>



<p className="retailer">

🏪 {deal.retailer}

</p>






<div className="money-grid">


<div>

<small>
Buy Price
</small>

<strong>

${deal.buy_price}

</strong>

</div>





<div>

<small>
Market Value
</small>

<strong>

${deal.market_price}

</strong>

</div>



</div>








<div className="profit-box">


<TrendingUp/>


<div>

<small>
Expected Profit
</small>


<h2>

+${deal.profit}

</h2>


</div>


</div>








<div className="stats-row">



<div>

<DollarSign/>

<p>
ROI
</p>

<strong>

{deal.roi}%

</strong>


</div>






<div>

<ShieldCheck/>

<p>
Risk
</p>


<strong>

LOW

</strong>


</div>






<div>

<Clock/>

<p>
Window

</p>


<strong>

3-7 Days

</strong>


</div>



</div>







<div className="ai-box">


<h3>
FlipIntel AI Analysis
</h3>


<p>

Recommendation:

</p>


<strong>

🟢 {deal.decision}

</strong>



<p>

Strong ROI opportunity detected.

Market value exceeds purchase price.

</p>


</div>





<button>

Analyze Deal

</button>



</div>


))}


</div>



</div>


);


}


export default Deals;