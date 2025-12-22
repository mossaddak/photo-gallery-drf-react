import { useState, useEffect } from "react";

import NavBar from "../navbar";
import LoginForm from "../forms/login";



function LoginPage() {
  return (
    <>
        <NavBar />
        <div className="container mt-5">
            <LoginForm />
        </div>
    </>
  );
}
export default LoginPage;
