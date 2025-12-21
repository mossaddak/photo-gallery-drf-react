import React, { useState, useRef } from "react";

import Buton from "../buttons";

function Form({ onSuccess }) {
    return (
        <div className="my-5 p-5 border rounded shadow bg-white">
            <h1 style={{ fontSize: "25px"}} className="mb-3">Login</h1>
            <form >
                <div className="text-center mb-4">
                    <input
                        type="text"
                        placeholder="Username"
                        className="form-control form-control-lg"
                        style={{ fontSize: "16px", padding: "8px" }}
                    />
                </div>

                <div className="text-center mb-4">
                    <input
                        type="password"
                        placeholder="Password"
                        className="form-control form-control-lg"
                        style={{ fontSize: "16px", padding: "8px" }}
                    />
                </div>

                <div className="" style={{ fontSize: "14px !important" }}>
                    <Buton title="Login"/>
                </div>
            </form>
        </div>
    );
}

export default Form;
