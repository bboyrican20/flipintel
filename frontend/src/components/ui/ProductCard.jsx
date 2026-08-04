import ProductImage from "./ProductImage";

function ProductCard({
    product,
    onAction,
    actionLabel = "View",
    loading = false
}) {

    if (!product) return null;

    return (

        <div className="product-card">

            <ProductImage
                image={product.image}
                title={product.product || product.name}
                brand={product.brand}
            />

            <div className="product-card-content">

                <div className="product-card-header">

                    <div>

                        <h2>
                            {product.product || product.name}
                        </h2>

                        <p>
                            {product.brand} • {product.category}
                        </p>

                    </div>

                    <div className="flip-score">

                        {Math.round(
                            product.flipintel_score ||
                            product.score ||
                            product.roi ||
                            0
                        )}

                    </div>

                </div>

                <div className="product-card-grid">

                    <div>
                        <span>Buy</span>
                        <strong>
                            ${product.buy_price ?? product.purchase_price ?? 0}
                        </strong>
                    </div>

                    <div>
                        <span>Market</span>
                        <strong>
                            ${product.market_price ?? product.expected_sale_price ?? 0}
                        </strong>
                    </div>

                    <div>
                        <span>Profit</span>
                        <strong className="profit">
                            +${product.profit ?? product.projected_profit ?? 0}
                        </strong>
                    </div>

                    <div>
                        <span>ROI</span>
                        <strong className="roi">
                            {Number(product.roi ?? 0).toFixed(2)}%
                        </strong>
                    </div>

                </div>

                <div className="recommendation">

                    {product.analysis?.recommendation ||
                     product.recommendation ||
                     "MONITOR"}

                </div>

                {onAction && (

                    <button
                        className="primary-button"
                        onClick={onAction}
                        disabled={loading}
                    >

                        {loading
                            ? "Working..."
                            : actionLabel}

                    </button>

                )}

            </div>

        </div>

    );

}

export default ProductCard;