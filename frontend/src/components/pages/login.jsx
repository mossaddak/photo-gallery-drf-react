import { useNavigate } from "react-router-dom";

import NavBar from "../navbar";
import LoginForm from "../forms/login";

function LoginPage() {
  const navigate = useNavigate();
  const handleLogin = () => {
    navigate("/", { replace: true });
  };
  return (
    <>
      <NavBar />
      <div className="container mt-5">
        <LoginForm onLogin={handleLogin} />
      </div>
    </>
  );
}
export default LoginPage;
