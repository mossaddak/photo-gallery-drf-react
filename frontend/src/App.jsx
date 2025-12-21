import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./components/pages/login";
import Home from "./components/pages/home";

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Home />,
    },
    {
      path: "/login",
      element: <Login />,
    },
  ]);

  return <RouterProvider router={router} />;
}

export default App;
