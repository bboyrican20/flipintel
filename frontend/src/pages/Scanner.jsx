import {
  Radio,
  ScanLine,
  Activity,
  Search,
  Zap
} from "lucide-react";


function Scanner(){


return (

<div className="scanner-page">


<header>

<h1>

📡 FlipIntel Scanner

</h1>


<p>

Real-time product intelligence engine

</p>


</header>





<section className="scanner-status-card">


<div className="online-indicator">

🟢 SCANNER ONLINE

</div>



<h2>

Retail Intelligence System Active

</h2>



<p>

Monitoring marketplaces and retailers for profitable opportunities.

</p>


</section>








<section className="scanner-grid">





<div className="scanner-box">


<ScanLine/>


<h3>

Products Scanned

</h3>


<strong>

4,821

</strong>


<p>

Today

</p>


</div>







<div className="scanner-box">


<Activity/>


<h3>

Opportunities Found

</h3>


<strong>

47

</strong>


<p>

AI detected

</p>


</div>








<div className="scanner-box">


<Zap/>


<h3>

High Confidence Deals

</h3>


<strong>

12

</strong>


<p>

Score 80+

</p>


</div>






</section>









<section className="scanner-feed">


<h2>

<Search/>

Live Scanner Feed

</h2>




<div className="scan-item">


<div>


<strong>

Makita 18V LXT Combo Kit

</strong>


<p>

Home Depot

</p>


</div>



<span className="scan-buy">

BUY NOW

</span>



</div>







<div className="scan-item">


<div>


<strong>

Milwaukee Tool Kit

</strong>


<p>

Lowes

</p>


</div>



<span className="scan-watch">

WATCH

</span>



</div>





</section>





</div>

);


}


export default Scanner;