import React from "react";

function Buton({ title, disabled }) {
  return (
    <>
      <button className="btn btn-success btn-lg px-3" disabled={disabled} style={{ fontSize: "16px"}}>
        {title}
      </button>
    </>
  );
}
export default Buton;
