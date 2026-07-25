import { useEffect, useState } from "react";
import axios from "axios";

import {
  Trophy,
  DollarSign,
  TrendingUp
} from "lucide-react";


const API = "http://localhost:8000";



function FlipHistory(){


const [sales,setSales] = useState([]);





useEffect(()=>{


async function loadSales(){


try{


const response = await axios.get(

`${API}/sales/`

);



setSales(

response.data.sales || []

);



}
catch(error){


console.error(

"Sales history error:",

error

);


}


}



loadSales();



},[]);








const totalProfit = sales.reduce(

(sum,item)=>

sum + Number(item.profit || 0),

0

);



const totalRevenue = sales.reduce(

(sum,item)=>

sum + Number(item.sale_price || 0),

0

);





return (

<div className="history-page">



<header>


<h1>

🏆 Flip History

</h1>


<p>

Completed flips and realized profits

</p>


</header>







<section className="stats">


<div className="card">

<DollarSign />


<h3>

Revenue

</h3>


<strong>

${totalRevenue}

</strong>


</div>






<div className="card">

<TrendingUp />


<h3>

Profit

</h3>


<strong className="profit">

+${totalProfit}

</strong>


</div>






<div className="card">

<Trophy />


<h3>

Completed Flips

</h3>


<strong>

{sales.length}

</strong>


</div>



</section>







<h2>

Completed Sales

</h2>








<div className="history-grid">



{

sales.map((sale)=>(


<div

className="history-card"

key={sale.inventory_id}

>



<h2>

{sale.product}

</h2>



<p>

🏪 {sale.retailer}

</p>



<p>

🏷️ {sale.brand}

</p>



<p>

📦 {sale.category}

</p>





<div>

Bought:

<strong>

${sale.purchase_price}

</strong>

</div>





<div>

Sold:

<strong>

${sale.sale_price}

</strong>

</div>





<div className="profit">

Profit:

<strong>

+${sale.profit}

</strong>

</div>





<div>

ROI:

<strong>

{sale.roi}%

</strong>

</div>





<p>

Status:

✅ {sale.status}

</p>





<p>

Sold:

{new Date(

sale.sold_at

).toLocaleDateString()}

</p>




</div>


))


}



</div>






</div>

);


}



export default FlipHistory;