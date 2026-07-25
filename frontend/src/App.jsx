import { useEffect, useState } from "react";
import axios from "axios";
import {
  Flame,
  Bell,
  TrendingUp,
  DollarSign,
  Target
} from "lucide-react";

import "./App.css";


const API = "http://localhost:8000";


function App() {

  const [deals, setDeals] = useState([]);
  const [alerts, setAlerts] = useState([]);
  const [opportunities, setOpportunities] = useState([]);
  const [analytics, setAnalytics] = useState(null);


  useEffect(() => {

    async function loadDashboard() {

      try {

        const [
          dealsRes,
          alertsRes,
          oppRes,
          analyticsRes
        ] = await Promise.all([

          axios.get(`${API}/deals/feed`),

          axios.get(`${API}/alerts/`),

          axios.get(`${API}/opportunities/`),

          axios.get(`${API}/analytics/dashboard`)

        ]);


        setDeals(
          dealsRes.data.hot_deals || []
        );


        setAlerts(
          alertsRes.data.alerts || []
        );


        setOpportunities(
          oppRes.data.opportunities || []
        );


        setAnalytics(
          analyticsRes.data
        );


      } catch(error) {

        console.error(
          "Dashboard error:",
          error
        );

      }

    }


    loadDashboard();

  }, []);



  return (

    <div className="dashboard">


      <header>

        <h1>
          FlipIntel
        </h1>

        <p>
          AI Product Flipping Intelligence Platform
        </p>

      </header>



      <section className="stats">


        <div className="card">

          <DollarSign />

          <h3>
            Revenue
          </h3>

          <strong>
            ${analytics?.financials?.revenue_generated || 0}
          </strong>

        </div>



        <div className="card">

          <TrendingUp />

          <h3>
            ROI
          </h3>

          <strong>
            {analytics?.financials?.roi || 0}%
          </strong>

        </div>



        <div className="card">

          <Target />

          <h3>
            Win Rate
          </h3>

          <strong>
            {analytics?.performance?.win_rate || 0}%
          </strong>

        </div>



        <div className="card">

          <Bell />

          <h3>
            Alerts
          </h3>

          <strong>
            {alerts.length}
          </strong>

        </div>


      </section>





      <section>

        <h2>
          <Flame />
          Hot Deals
        </h2>


        <div className="grid">

        {deals.map((deal)=>(

          <div className="deal" key={deal.product_id}>


            <h3>
              {deal.product}
            </h3>


            <p>
              Retailer: {deal.retailer}
            </p>


            <h1>
              Score {deal.score}/100
            </h1>


            <p>
              Buy: ${deal.buy_price}
            </p>


            <p>
              Market: ${deal.market_price}
            </p>


            <p className="profit">

              Profit:
              ${deal.profit}

            </p>


            <p>

              ROI:
              {deal.roi}%

            </p>


          </div>

        ))}

        </div>

      </section>





      <section>

        <h2>
          🚨 Alert Center
        </h2>


        {alerts.map(alert=>(

          <div className="alert" key={alert.product_id}>

            <strong>
              {alert.type}
            </strong>

            <p>
              {alert.message}
            </p>


          </div>

        ))}


      </section>





      <section>

        <h2>
          💰 Opportunities
        </h2>


        {opportunities.map(item=>(

          <div className="opportunity" key={item.product_id}>


            <strong>
              {item.product}
            </strong>


            <span>
              Score: {item.flip_score}
            </span>


            <span>
              Profit: ${item.expected_profit}
            </span>


          </div>


        ))}


      </section>



    </div>

  );

}


export default App;