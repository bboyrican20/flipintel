import {
  useState
} from "react";


import axios from "axios";


import {
  ScanLine,
  Activity,
  Zap,
  Search,
  PackagePlus
} from "lucide-react";



const API = "http://localhost:8000";



function Scanner(){


const [barcode,setBarcode] = useState("");

const [buyPrice,setBuyPrice] = useState("");

const [retailer,setRetailer] = useState("");


const [result,setResult] = useState(null);

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

product:

result.product,


retailer:

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

📡 FlipIntel Scanner

</h1>


<p>

Real-time product intelligence engine

</p>


</header>







<section className="scanner-box">


<h2>

<ScanLine/>

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

onClick={scanProduct}

disabled={loading}

>


{

loading

?

"Analyzing..."

:

"🚀 Analyze Product"

}


</button>



</section>










{

result &&


<section className="scanner-result">


<h2>

<Search/>

Analysis Result

</h2>





<h3>

{result.product}

</h3>





<p>

Brand:

<strong>

{" "}{result.brand}

</strong>

</p>





<p>

Category:

<strong>

{" "}{result.category}

</strong>

</p>





<p>

Market Price:

<strong>

${result.market_price}

</strong>

</p>





<p>

Profit:

<strong className="profit">

+${result.profit}

</strong>

</p>





<p>

ROI:

<strong>

{result.roi.toFixed(2)}%

</strong>

</p>






<h2>

{result.analysis?.recommendation}

</h2>





<p>

{result.deal_explanation?.summary}

</p>






<button

className="inventory-button"

onClick={addInventory}

disabled={adding}

>


<PackagePlus/>


{

adding

?

"Adding..."

:

"Add To Inventory"

}


</button>





</section>


}










<section className="scanner-grid">



<div className="scanner-box">


<ScanLine/>


<h3>

Scanner Engine

</h3>


<strong>

ONLINE

</strong>


</div>







<div className="scanner-box">


<Activity/>


<h3>

AI Analysis

</h3>


<strong>

ACTIVE

</strong>


</div>







<div className="scanner-box">


<Zap/>


<h3>

Decision Engine

</h3>


<strong>

READY

</strong>


</div>



</section>






</div>


);


}


export default Scanner;