import React from "react";

export default function ProductImage({ image, title }) {

  return (
    <div className="product-image">

      {image ? (
        <img
          src={image}
          alt={title}
        />
      ) : (
        <div className="image-placeholder">
          No Image
        </div>
      )}

    </div>
  );
}