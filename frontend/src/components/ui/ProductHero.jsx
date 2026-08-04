import ROIBadge from "./ROIBadge";


function ProductHero({ product }) {


    return (

        <div className="product-hero premium-product-hero">



            <div className="product-image-box premium-image">


                📦


            </div>







            <div className="product-info">





                <div className="hero-top">



                    <span className="deal-fire premium-fire">


                        🔥 HOT DEAL


                    </span>




                    <ROIBadge

                        roi={product.roi}

                    />


                </div>







                <h1>


                    {product.product}


                </h1>







                <p className="brand">


                    {product.brand || "Premium Product"}


                </p>







            </div>






        </div>

    );

}


export default ProductHero;