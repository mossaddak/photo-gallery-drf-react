import React from "react";

import Buton from "./buttons";

function Pagination() {
  return (
    <nav aria-label="Page navigation example">
      <ul className="pagination">
        <li className="page-item m-1">
          <Buton title="<" />
        </li>
        <li className="page-item m-1">
          <Buton title="1" />
        </li>
        <li className="page-item m-1">
          <Buton title="2" />
        </li>
        <li className="page-item m-1">
          <Buton title="3" />
        </li>
        <li className="page-item m-1">
          <Buton title=">" />
        </li>
      </ul>
    </nav>
  );
}

export default Pagination;
