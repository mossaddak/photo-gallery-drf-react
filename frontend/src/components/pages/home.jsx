import { useState, useEffect } from "react";

import Card from "../cards";
import Form from "../forms/cards";
import Pagination from "../paginations";
import NavBar from "../navbar";

function App() {
  const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;
  const [fileItemQuote, setFileItemQuote] = useState([]);
  const token = localStorage.getItem("access_token");

  const fetchFiles = async () => {
    const response = await fetch(`${API_BASE_URL}/me/files?page_size=12`, {
      headers: {
        "Authorization": `Bearer ${token}`,
      },
    });
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
