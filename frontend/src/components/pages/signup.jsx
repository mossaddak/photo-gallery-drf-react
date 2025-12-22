import { useState, useEffect } from "react";

import NavBar from "../navbar";
import SignUpForm from "../forms/signup";



function SignUp() {
    return (
        <>
            <NavBar />
            <div className="container mt-5">
                <SignUpForm />
            </div>
        </>
    );
}
export default SignUp;
