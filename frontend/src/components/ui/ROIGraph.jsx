import {
    BarChart,
    Bar,
    XAxis,
    YAxis,
    Tooltip,
    ResponsiveContainer
} from "recharts";



function ROIGraph(){


    const data=[


        {
            name:"Tools",
            roi:187
        },


        {
            name:"Electronics",
            roi:142
        },


        {
            name:"Home",
            roi:96
        }


    ];



    return (


        <div className="chart-card">


            <h2>

                🚀 ROI Performance

            </h2>



            <ResponsiveContainer

                width="100%"

                height={300}

            >


                <BarChart

                    data={data}

                >


                    <XAxis

                        dataKey="name"

                    />



                    <YAxis />



                    <Tooltip />



                    <Bar

                        dataKey="roi"

                    />


                </BarChart>


            </ResponsiveContainer>


        </div>


    );


}


export default ROIGraph;