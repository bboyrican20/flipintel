import {
  NavLink
} from "react-router-dom";


import {
  Flame,
  LayoutDashboard,
  ScanLine,
  Package,
  BarChart3
} from "lucide-react";



function Sidebar(){


  return (


    <aside className="sidebar">


      <h2>

        🔥 FlipIntel

      </h2>





      <nav>



        <NavLink to="/">

          <LayoutDashboard />

          Dashboard

        </NavLink>





        <NavLink to="/deals">

          <Flame />

          Hot Deals

        </NavLink>





        <NavLink to="/scanner">

          <ScanLine />

          Scanner

        </NavLink>





        <NavLink to="/inventory">

          <Package />

          Inventory

        </NavLink>





        <NavLink to="/analytics">

          <BarChart3 />

          Analytics

        </NavLink>



      </nav>






      <div className="scanner-status">


        🟢 Scanner Online


      </div>



    </aside>


  );


}


export default Sidebar;