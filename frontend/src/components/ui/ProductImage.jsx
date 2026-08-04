import React, { useState } from "react";

export default function ProductImage({ image, title, brand }) {

    const [error, setError] = useState(false);

    const initials = title
        ? title
            .split(" ")
            .slice(0, 2)
            .map(word => word[0])
            .join("")
            .toUpperCase()
        : "?";

    return (

        <div className="product-image">

            {!image || error ? (

                <div className="image-placeholder">

                    <div className="placeholder-icon">
                        📦
                    </div>

                    <div className="placeholder-title">
                        {initials}
                    </div>

                    {brand && (
                        <div className="placeholder-brand">
                            {brand}
                        </div>
                    )}

                </div>

            ) : (

                <img
                    src={image}
                    alt={title}
                    loading="lazy"
                    onError={() => setError(true)}
                />

            )}

        </div>

    );

}