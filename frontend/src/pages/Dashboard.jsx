import { useEffect, useState } from "react";
import axios from "axios";

import {
  DollarSign,
  TrendingUp,
  Target,
  Bell,
  Flame,
  Trophy,
  ShieldCheck,
  Clock
} from "lucide-react";


const API = "http://localhost:8000";



function Dashboard(){


const [deals,setDeals] = useState([]);

const [alerts,setAlerts] = useState([]);

const [analytics,setAnalytics] = useState(null);





useEffect(()=>{


async function loadDashboard(){


try{


const [

dealsRes,

alertsRes,

analyticsRes


] = await Promise.all([


axios.get(`${API}/deals/feed`),


axios.get(`${API}/alerts/`),


axios.get(`${API}/analytics/dashboard`)


]);



setDeals(

dealsRes.data.hot_deals || []

);



setAlerts(

alertsRes.data.alerts || []

);



setAnalytics(

analyticsRes.data

);



}

catch(error){


console.error(

"Dashboard Error:",

error

);


}



}


loadDashboard();



},[]);





const bestDeal = deals[0];






return (

<div className="dashboard-home">





<header className="dashboard-header">


<h1>

🔥 FlipIntel Dashboard

</h1>


<p>

AI Product Flipping Intelligence Platform

</p>


</header>







<section className="stats">





<div className="card dashboard-card">


<DollarSign/>


<h3>

Capital Invested

</h3>


<strong>

${analytics?.financials?.capital_invested || 0}

</strong>


</div>






<div className="card dashboard-card">


<TrendingUp/>


<h3>

Revenue Generated

</h3>


<strong>

${analytics?.financials?.revenue_generated || 0}

</strong>


</div>







<div className="card dashboard-card">


<Trophy/>


<h3>

Realized Profit

</h3>


<strong className="profit">

+

${analytics?.financials?.realized_profit || 0}

</strong>


</div>







<div className="card dashboard-card">


<Target/>


<h3>

ROI Performance

</h3>


<strong>

{analytics?.financials?.roi || 0}%

</strong>


</div>



</section>










<section className="feature-grid">





<div className="featured-deal">


<h2>

🔥 Best Opportunity

</h2>



{bestDeal && (

<>



<div className="decision">

{bestDeal.decision}

</div>



<h1>

{bestDeal.product}

</h1>



<p>

🏪 {bestDeal.retailer}

</p>




<div className="big-profit">


Expected Profit

<h2>

+${bestDeal.profit}

</h2>


</div>





<div className="deal-mini-stats">


<div>

<small>
Flip Score
</small>

<strong>

{bestDeal.score}/100

</strong>

</div>



<div>

<small>
ROI
</small>

<strong>

{bestDeal.roi}%

</strong>

</div>



<div>

<small>
Risk
</small>

<strong>

LOW

</strong>

</div>


</div>




</>

)}



</div>









<div className="ai-analysis">


<h2>

🤖 FlipIntel AI Analysis

</h2>


<p>

Recommendation:

</p>


<h3>

🟢 {bestDeal?.decision || "WAITING"}

</h3>



<p>

Strong ROI opportunity detected.

Market value exceeds purchase price.

</p>




<div className="analysis-row">


<ShieldCheck/>

Risk Level:

<strong>

LOW

</strong>


</div>




<div className="analysis-row">


<Clock/>

Estimated Flip Window:

<strong>

3-7 Days

</strong>


</div>



</div>





</section>










<section>


<h2>

🚨 Live Alerts

</h2>



<div className="alerts-dashboard">


{alerts.map(alert=>(


<div 
className="alert"
key={alert.product_id}
>


<strong>

{alert.type}

</strong>


<p>

{alert.message}

</p>


</div>


))}


</div>



</section>






</div>

);


}


export default Dashboard;