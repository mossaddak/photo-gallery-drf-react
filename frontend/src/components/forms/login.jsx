import React, { useState } from "react";

import Button from "../buttons";

function LoginForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    const handleLoginSubmit = async (e) => {
        e.preventDefault();

        // Fetch API to login
        const login_response = await fetch(`${API_BASE_URL}/accounts/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        const login_response_data = await login_response.json();

        console.log("Login response:=====================+>", login_response_data);

        // If login is successful, store tokens and redirect
        if (login_response.ok) {
            localStorage.setItem("access_token", login_response_data.access);
            localStorage.setItem("refresh_token", login_response_data.refresh);

            // Fetch login user
            const user_response = await fetch(`${API_BASE_URL}/me?is_header=true`, {
                headers: {
                    "Authorization": `Bearer ${login_response_data.access}`,
                },
            });
            localStorage.setItem("user", JSON.stringify(await user_response.json()));
            onLogin();
        } else {
            setError(login_response_data.detail || "Login failed");
        }
    }

    return (
        <div className="my-5 p-5 border rounded shadow bg-white">
            <h1 style={{ fontSize: "25px" }} className="mb-3">Login</h1>
            <form onSubmit={handleLoginSubmit}>
                <div className="text-center mb-4">
                    <input
                        type="text"
                        placeholder="Username"
                        value={username}
                        onChange={(e) => setUsername(e.target.value)}
                        className="form-control form-control-lg"
                        style={{ fontSize: "16px", padding: "8px" }}
                        required
                    />
                </div>

                <div className="text-center mb-4">
                    <input
                        type="password"
                        placeholder="Password"
                        onChange={(e) => setPassword(e.target.value)}
                        value={password}
                        className="form-control form-control-lg"
                        style={{ fontSize: "16px", padding: "8px" }}
                        required
                    />
                </div>

                <div className="" style={{ fontSize: "14px !important" }}>
                    <Button title="Login" />
                </div>
            </form>
        </div>
    );
}

export default LoginForm;
