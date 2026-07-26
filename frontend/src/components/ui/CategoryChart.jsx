import {
    PieChart,
    Pie,
    Cell,
    Tooltip,
    ResponsiveContainer
} from "recharts";



function CategoryChart(){


    const data=[


        {
            name:"Tools",
            value:45
        },


        {
            name:"Electronics",
            value:30
        },


        {
            name:"Home",
            value:25
        }


    ];



    return (


        <div className="chart-card">


            <h2>

                🏆 Top Categories

            </h2>




            <ResponsiveContainer

                width="100%"

                height={300}

            >


                <PieChart>


                    <Pie

                        data={data}

                        dataKey="value"

                        nameKey="name"

                        outerRadius={100}

                    >


                        {
                            data.map(
                                (entry,index)=>(

                                <Cell

                                    key={index}

                                />

                                )
                            )
                        }


                    </Pie>


                    <Tooltip />


                </PieChart>


            </ResponsiveContainer>


        </div>


    );


}


export default CategoryChart;