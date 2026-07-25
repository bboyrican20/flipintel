import { useEffect, useState } from "react";
import axios from "axios";

import {
  Package,
  DollarSign,
  TrendingUp
} from "lucide-react";


const API = "http://localhost:8000";


function Inventory(){


  const [inventory,setInventory] = useState([]);



  useEffect(()=>{


    async function loadInventory(){


      try{


        const response = await axios.get(
          `${API}/inventory/`
        );


        setInventory(
          response.data.inventory || []
        );


      }catch(error){


        console.error(
          "Inventory error:",
          error
        );


      }


    }


    loadInventory();


  },[]);





  const capital = inventory.reduce(
    (total,item)=>
      total + (item.purchase_price * item.quantity),
    0
  );



  const revenue = inventory.reduce(
    (total,item)=>
      total + (item.expected_sale_price * item.quantity),
    0
  );



  const profit = inventory.reduce(
    (total,item)=>
      total + (item.projected_profit * item.quantity),
    0
  );





  return (

    <section className="inventory-panel">


      <h2>

        <Package />

        Inventory Command Center

      </h2>





      <div className="inventory-stats">


        <div className="inventory-card">

          <h3>
            Items Owned
          </h3>

          <strong>
            {inventory.length}
          </strong>

        </div>




        <div className="inventory-card">

          <h3>
            Capital Invested
          </h3>

          <strong>
            ${capital}
          </strong>

        </div>




        <div className="inventory-card">

          <h3>
            Expected Revenue
          </h3>

          <strong>
            ${revenue}
          </strong>

        </div>




        <div className="inventory-card">

          <h3>
            Projected Profit
          </h3>

          <strong className="green">

            +${profit}

          </strong>

        </div>


      </div>






      <div className="inventory-table">


        <h3>
          Inventory Items
        </h3>



        {inventory.map(item=>(


          <div
            className="inventory-row"
            key={item.inventory_id}
          >


            <strong>
              {item.product}
            </strong>



            <span>
              Qty: {item.quantity}
            </span>



            <span>
              Cost: ${item.purchase_price}
            </span>



            <span>
              Value: ${item.expected_sale_price}
            </span>



            <span className="green">

              Profit:
              +${item.projected_profit}

            </span>



          </div>


        ))}



      </div>



    </section>

  );

}



export default Inventory;