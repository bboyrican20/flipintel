import {
  useEffect,
  useState
} from "react";


import axios from "axios";


import {
  BarChart3,
  TrendingUp,
  DollarSign,
  Package,
  Trophy
} from "lucide-react";



const API = "http://localhost:8000";



function Analytics(){


const [data,setData] = useState(null);





useEffect(()=>{


async function loadAnalytics(){


try{


const response = await axios.get(

`${API}/analytics/dashboard`

);



setData(

response.data

);



}
catch(error){


console.error(

"Analytics error:",
error

);


}


}



loadAnalytics();



},[]);






if(!data){


return (

<div>

<h1>

<BarChart3 />

Loading Analytics...

</h1>

</div>

);


}







return (


<div className="analytics-page">





<header>


<h1>

<BarChart3 />

 Analytics Intelligence

</h1>


<p>

FlipIntel business performance overview

</p>


</header>







<section className="stats">






<div className="card">


<DollarSign />


<h3>

Capital Invested

</h3>


<strong>

${data.financials.capital_invested}

</strong>


</div>







<div className="card">


<DollarSign />


<h3>

Revenue Generated

</h3>


<strong>

${data.financials.revenue_generated}

</strong>


</div>








<div className="card">


<TrendingUp />


<h3>

Realized Profit

</h3>


<strong className="profit">

+${data.financials.realized_profit}

</strong>


</div>







<div className="card">


<TrendingUp />


<h3>

ROI Performance

</h3>


<strong>

{data.financials.roi}%

</strong>


</div>




</section>








<section className="card">


<h2>

📦 Portfolio

</h2>



<p>

Total Items:

<strong>

{" "}{data.portfolio.total_items}

</strong>

</p>



<p>

Active Inventory:

<strong>

{" "}{data.portfolio.active_inventory}

</strong>

</p>



<p>

Completed Flips:

<strong>

{" "}{data.portfolio.sold_flips}

</strong>

</p>



</section>









<section className="card">


<h2>

🏆 Best Flip

</h2>



{

data.best_flip ?

<>

<h3>

{data.best_flip.product}

</h3>


<p>

Profit:

<strong>

+${data.best_flip.profit}

</strong>

</p>


<p>

ROI:

<strong>

{data.best_flip.roi}%

</strong>

</p>


</>

:

<p>

No completed flips yet.

</p>

}




</section>









<section className="card">


<h2>

🔥 Top Brands

</h2>


{

data.top_brands?.map(

(brand,index)=>(


<p key={index}>


{brand.brand}

:

<strong>

{" "}{brand.profit}

</strong>


</p>


)

)


}



</section>









<section className="card">


<h2>

🏪 Retailer Performance

</h2>



{

data.retailers?.map(

(store,index)=>(


<p key={index}>


{store.retailer}


:

<strong>

{" "}{store.profit}

</strong>


</p>


)

)


}



</section>







</div>


);


}



export default Analytics;