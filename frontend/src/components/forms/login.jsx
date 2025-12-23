import React, { useState } from "react";

import Button from "../buttons";

function LoginForm({ onLogin }) {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL;

    const handleSubmit = async (e) => {
        e.preventDefault();

        // Fetch API to login
        const response = await fetch(`${API_BASE_URL}/accounts/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, password }),
        });
        const _data = await response.json();

        // If login is successful, store tokens and redirect
        if (response.ok) {
            localStorage.setItem("access_token", _data.access);
            localStorage.setItem("refresh_token", _data.refresh);

            // Fetch login user
            const user_response = await fetch(`${API_BASE_URL}/me?is_header=true`, {
                headers: {
                    "Authorization": `Bearer ${_data.access}`,
                },
            });
            localStorage.setItem("user", JSON.stringify(await user_response.json()));
            onLogin();
        } else {
            setError(_data.detail || "Login failed");
        }
    }

    return (
        <div className="my-5 p-5 border rounded shadow bg-white">
            <h1 style={{ fontSize: "25px" }} className="mb-3">Login</h1>
            <form onSubmit={handleSubmit}>
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
