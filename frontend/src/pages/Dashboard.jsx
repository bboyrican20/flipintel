import {
    useEffect,
    useState
} from "react";

import axios from "axios";


import {
    DollarSign,
    TrendingUp,
    Target,
    Trophy,
    ShieldCheck,
    Clock
} from "lucide-react";


import ProfitChart from "../components/ui/ProfitChart";
import ROIGraph from "../components/ui/ROIGraph";
import CategoryChart from "../components/ui/CategoryChart";
import AIScore from "../components/ui/AIScore";


const API = "http://localhost:8000";



function Dashboard(){


    const [analytics,setAnalytics] = useState(null);

    const [deals,setDeals] = useState([]);

    const [alerts,setAlerts] = useState([]);

    const [aiAnalysis,setAiAnalysis] = useState(null);



    useEffect(()=>{


        async function loadDashboard(){


            try{


                const [

                    analyticsRes,

                    dealsRes,

                    alertsRes,

                    aiRes


                ] = await Promise.all([


                    axios.get(
                        `${API}/analytics/dashboard`
                    ),


                    axios.get(
                        `${API}/dashboard/top-deals`
                    ),


                    axios.get(
                        `${API}/alerts/`
                    ),


                    axios.get(
                        `${API}/dashboard/ai`
                    )


                ]);



                setAnalytics(
                    analyticsRes.data
                );


                setDeals(
                    dealsRes.data.top_deals || []
                );


                setAlerts(
                    alertsRes.data.alerts || []
                );


                setAiAnalysis(
                    aiRes.data
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
                    🔥 FlipIntel Pro Dashboard
                </h1>


                <p>
                    AI Product Flipping Intelligence Platform
                </p>


            </header>







            <section className="stats-grid">



                <div className="stat-card">

                    <DollarSign/>

                    <h3>
                        Capital Invested
                    </h3>


                    <strong>

                        $
                        {analytics?.financials?.capital_invested || 0}

                    </strong>


                </div>






                <div className="stat-card">


                    <TrendingUp/>


                    <h3>
                        Revenue Generated
                    </h3>


                    <strong>

                        $
                        {analytics?.financials?.revenue_generated || 0}

                    </strong>


                </div>







                <div className="stat-card">


                    <Trophy/>


                    <h3>
                        Realized Profit
                    </h3>


                    <strong className="profit">

                        +
                        $
                        {analytics?.financials?.realized_profit || 0}

                    </strong>


                </div>







                <div className="stat-card">


                    <Target/>


                    <h3>
                        ROI Performance
                    </h3>


                    <strong className="roi">


                        {analytics?.financials?.roi || 0}%


                    </strong>


                </div>



            </section>









            <section className="charts-grid">


                <ProfitChart/>


                <ROIGraph/>


                <CategoryChart/>


            </section>









            <section className="feature-grid">



                <div className="featured-deal">


                    <h2>
                        📦 Inventory Status
                    </h2>



                    <h1>

                        {
                        analytics?.portfolio?.active_inventory || 0
                        }

                        {" "}
                        Active Flips

                    </h1>



                    <p>

                        Completed:

                        {" "}

                        {
                        analytics?.portfolio?.sold_flips || 0
                        }

                        flips

                    </p>






                    <div className="big-profit">


                        Projected Profit


                        <h2 className="profit">


                            +$

                            {
                            analytics?.financials?.projected_profit || 0
                            }


                        </h2>


                    </div>




                </div>









                <div className="ai-analysis">


                    <h2>
                        🤖 FlipIntel AI Analysis
                    </h2>



                    <p>
                        Recommendation:
                    </p>



                    <h3>

                        🟢

                        {
                        aiAnalysis?.recommendation ||
                        bestDeal?.recommendation ||
                        "MONITOR INVENTORY"
                        }

                    </h3>




                    <div className="analysis-row">


                        <ShieldCheck/>


                        Risk Level:


                        <strong>

                            {
                            aiAnalysis?.risk ||
                            "LOW"
                            }

                        </strong>


                    </div>







                    <div className="analysis-row">


                        <Clock/>


                        Estimated Flip Window:


                        <strong>

                            {
                            aiAnalysis?.flip_window ||
                            "3-7 Days"
                            }

                        </strong>


                    </div>



                </div>



            </section>









            <section className="ai-section">


    <AIScore


        score={

            aiAnalysis?.confidence ||

            bestDeal?.flipintel_score ||

            0

        }



        reasons={

            aiAnalysis?.reasons ||

            [

                "Inventory tracked",

                "ROI calculated",

                "Sales performance monitored"

            ]

        }



        recommendation={

            aiAnalysis?.recommendation ||

            bestDeal?.recommendation ||

            "WAITING"

        }


    />


</section>









            <section>


                <h2>
                    🚨 Live Alerts
                </h2>



                <div className="alerts-dashboard">


                {

                alerts.map(alert=>(


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


                ))

                }


                </div>



            </section>





        </div>

    );


}



export default Dashboard;