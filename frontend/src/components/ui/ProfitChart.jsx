import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer
} from "recharts";



function ProfitChart(){


    const data = [


        {
            month:"Jan",
            profit:1200
        },


        {
            month:"Feb",
            profit:2400
        },


        {
            month:"Mar",
            profit:3900
        },


        {
            month:"Apr",
            profit:5200
        },


        {
            month:"May",
            profit:7400
        }


    ];




    return (


        <div className="chart-card">


            <h2>

                📈 Profit Growth

            </h2>



            <ResponsiveContainer

                width="100%"

                height={300}

            >


                <LineChart

                    data={data}

                >


                    <CartesianGrid

                        strokeDasharray="3 3"

                    />



                    <XAxis

                        dataKey="month"

                    />



                    <YAxis />



                    <Tooltip />



                    <Line

                        type="monotone"

                        dataKey="profit"

                        strokeWidth={4}

                        dot={{r:5}}

                    />


                </LineChart>


            </ResponsiveContainer>


        </div>


    );


}


export default ProfitChart;