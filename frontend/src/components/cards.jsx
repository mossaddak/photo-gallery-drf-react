import React from "react";

import Buton from "./buttons";

function Card({ card_contents }) {
  return (
    <div className="d-flex flex-wrap justify-content-center">
      {card_contents.map((card_content) => (
        <div className="card p-2 m-3" style={{ width: "18rem" }}>
          <img
            src={card_content.file}
            className="card-img-top"
            style={{ height: "200px", objectFit: "cover" }}
            alt={`A image for ${card_content.title}`}
          />
          <h5 className="card-title mt-3">{card_content.title}</h5>
          <p className="card-text">{card_content.description}</p>
          <Buton title="Go Somewhere" />
        </div>
      ))}
    </div>
  );
}

export default Card;
