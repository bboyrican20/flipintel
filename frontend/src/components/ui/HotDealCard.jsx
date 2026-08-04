import { useState, useEffect } from "react";
import axios from "axios";

import DealAI from "./DealAI";
import AISummary from "./AISummary";
import AIGrade from "./AIGrade";
import RiskAnalysis from "./RiskAnalysis";
import FlipStrategy from "./FlipStrategy";
import MarketplaceAI from "./MarketplaceAI";
import ProductHero from "./ProductHero";
import FlipScore from "./FlipScore";
import ProfitOpportunity from "./ProfitOpportunity";
import DealBreakdown from "./DealBreakdown";
import AIReasoning from "./AIReasoning";
import FlipScoreBreakdown from "./FlipScoreBreakdown";


const API = "http://localhost:8000";



function HotDealCard({ product, onBuy }) {


    const [expanded, setExpanded] = useState(false);

    const [aiAnalysis, setAiAnalysis] = useState(null);





    useEffect(() => {


        async function loadAI() {


            try {


                const response = await axios.get(

                    `${API}/deal-ai/${product.product_id}`

                );


                setAiAnalysis(response.data);


            }

            catch(error) {


                console.error(

                    "AI Analysis Error:",

                    error

                );


            }


        }





        if(product.product_id) {

            loadAI();

        }



    }, [product.product_id]);







    const score =

        product.deal_score ??

        product.flipintel_score ??

        aiAnalysis?.score ??

        61;







    return (


        <div className="hot-deal-card premium-deal-card">





            <div className="deal-header-v2">


                <ProductHero

                    product={product}

                />


                <FlipScore

                    score={score}

                />


            </div>









            <div className="deal-prices premium-metrics">



                <div className="metric-card">


                    <span>💰 Profit</span>


                    <strong className="profit">

                        +${

                            product.profit ??

                            aiAnalysis?.metrics?.profit ??

                            0

                        }


                    </strong>


                </div>







                <div className="metric-card">


                    <span>🏷 Buy Price</span>


                    <strong>

                        ${

                            product.buy_price ??

                            aiAnalysis?.metrics?.purchase_price ??

                            0

                        }


                    </strong>


                </div>







                <div className="metric-card">


                    <span>🌎 Market Value</span>


                    <strong>

                        ${

                            product.market_price ??

                            aiAnalysis?.metrics?.expected_sale ??

                            0

                        }


                    </strong>


                </div>







                <div className="metric-card">


                    <span>📈 ROI</span>


                    <strong>

                        {

                            Number(

                                product.roi ??

                                aiAnalysis?.metrics?.roi ??

                                0

                            ).toFixed(2)

                        }%

                    </strong>


                </div>


            </div>









            <div className="premium-recommendation">


                <div className="recommendation-icon">

                    🧠

                </div>



                <div className="recommendation-content">


                    <strong>

                        AI Recommendation

                    </strong>



                    <p>

                        {

                            aiAnalysis?.recommendation ??

                            product.recommendation ??

                            "Strong Buy"

                        }


                    </p>


                </div>


            </div>









            <div className="deal-actions">



                <button

                    className="buy-button premium-buy"

                    onClick={onBuy}

                >

                    🛒 BUY THIS DEAL

                </button>







                <button

                    className="analysis-toggle"

                    onClick={() => setExpanded(!expanded)}

                >

                    {

                        expanded

                        ? "▲ HIDE ANALYSIS"

                        : "▼ VIEW ANALYSIS"

                    }


                </button>


            </div>









            {expanded && (


                <div className="deal-analysis">



                    <div className="analysis-header">


                        🧠 FlipIntel AI Intelligence Report


                    </div>







                    <DealAI

                        analysis={aiAnalysis}

                    />







                    <AISummary

                        summary={aiAnalysis?.summary}

                    />







                    <AIGrade

                        grade={aiAnalysis?.grade}

                    />







                    <FlipScoreBreakdown

                        product={product}

                        analysis={aiAnalysis}

                    />







                    <ProfitOpportunity

                        product={product}

                    />







                    <DealBreakdown

                        product={product}

                    />







                    <MarketplaceAI

                        marketplace={aiAnalysis?.marketplace}

                    />







                    <AIReasoning

                        product={product}

                        analysis={aiAnalysis}

                    />







                    <RiskAnalysis

                        riskAnalysis={aiAnalysis?.risk_analysis}

                    />







                    <FlipStrategy

                        strategy={aiAnalysis?.strategy}

                    />





                </div>


            )}






        </div>


    );


}


export default HotDealCard;