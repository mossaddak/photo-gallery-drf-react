import { useState, useEffect } from "react";

import Card from "../cards";
import Form from "../forms/cards";
import Pagination from "../paginations";
import NavBar from "../navbar";



function App() {


  const [fileItemQuote, setFileItemQuote] = useState([]);

  const fetchFiles = async () => {
    const response = await fetch("http://127.0.0.1:8000/api/v1/me/files");
    if (!response.ok) throw new Error("Failed to fetch");
    const data = await response.json();
    setFileItemQuote(data.results);
  };

  useEffect(() => {
    fetchFiles();
  }, []);


  return (
    <>
      <NavBar />
      <div className="container">
        <h4 className="text-center my-4">My File Gallery</h4>
        <hr />
        <div className="mb-5">
          <Form onSuccess={fetchFiles} />
        </div>
        <hr />
        <div>
          <Card card_contents={fileItemQuote} />
        </div>
        <div className="d-flex justify-content-end">
          <Pagination />
        </div>
      </div>

    </>
  );
}
export default App;
