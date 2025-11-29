import Card from "./components/cards";
import { useState, useEffect } from "react";

function App() {
  const [fileItemQuote, setFileItemQuote] = useState(null);
      const fetchFileItemQuote = async () => {
        const res = await fetch('http://127.0.0.1:8000/api/v1/files');
        if (!res.ok) throw new Error('Failed to fetch');
        const data = await res.json();
        setFileItemQuote(data);
    };

  useEffect(() => {
    fetchFileItemQuote();
  }, []);

  const cards = Array.isArray(fileItemQuote) ? fileItemQuote : [];

  return (
    <div className="p-5">
      <h4 className="text-center">New Cards</h4>
      <hr />
      <Card card_contents={cards} />
    </div>
  );
}
export default App;