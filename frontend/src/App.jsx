import Dashboard from "./pages/Dashboard";
import Scanner from "./pages/Scanner";
import InventoryPage from "./pages/InventoryPage";
import Analytics from "./pages/Analytics";
import Deals from "./pages/Deals";
import FlipHistory from "./pages/FlipHistory";


import {
  Routes,
  Route
} from "react-router-dom";


import Sidebar from "./components/Sidebar";


import "./App.css";



function App(){


  return (


    <div className="app-layout">


      <Sidebar />



      <main className="dashboard">


        <Routes>


          <Route
            path="/"
            element={<Dashboard />}
          />



          <Route
            path="/scanner"
            element={<Scanner />}
          />



          <Route
            path="/inventory"
            element={<InventoryPage />}
          />



          <Route
            path="/analytics"
            element={<Analytics />}
          />



          <Route
            path="/deals"
            element={<Deals />}
          />



          <Route
            path="/history"
            element={<FlipHistory />}
          />



        </Routes>



      </main>



    </div>


  );


}


export default App;