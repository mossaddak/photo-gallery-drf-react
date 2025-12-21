import React, { useState, useRef } from "react";

import Buton from "../buttons";

function Form({ onSuccess }) {
  const [files, setFiles] = useState([]);
  const [title, setTitle] = useState("");
  const fileInputRef = useRef(null);

  const handleTitleChange = (event) => {
    setTitle(event.target.value);
  };

  const handleFileChange = (event) => {
    const selectedFiles = Array.from(event.target.files);
    setFiles(selectedFiles);
  };

  const handleSubmit = async (data) => {
    data.preventDefault();
    console.log("Uploading files:",);
    const uploadPromises = files.map(async (file) => {
      const description = file.name;

      const formData = new FormData();
      formData.append("title", title);
      formData.append("description", description);
      formData.append("file", file);

      const response = await fetch("http://127.0.0.1:8000/api/v1/me/files", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const err = await response.json().catch(() => ({}));
        throw new Error(`${file.name} → ${err.message || "Failed"}`);
      }
      return response.json();
    });

    await Promise.all(uploadPromises);

    setFiles([]);
    if (fileInputRef.current) fileInputRef.current.value = "";
    if (onSuccess) onSuccess();
  };

  return (
    <div className="my-5 p-5 border rounded shadow bg-white">
      <form onSubmit={handleSubmit}>
        <div className="text-center mb-4">
          <input
            type="text"
            placeholder="Title"
            className="form-control form-control-lg"
            onChange={handleTitleChange}
            style={{ fontSize: "16px", padding: "8px" }}
            value={title}
          />
        </div>

        <p className="text-center text-success" style={{ fontSize: "14px"}}>
          Select many files → Each file becomes 1 record with auto
          description
        </p>
        <div className="text-center mb-4">
          <input
            ref={fileInputRef}
            type="file"
            className="form-control form-control-lg"
            multiple
            accept="image/*,.pdf,.doc,.docx"
            onChange={handleFileChange}
            style={{ fontSize: "16px", padding: "8px" }}
          />
          <small className="text-muted d-block mt-2" style={{ fontSize: "14px"}}>
            Hold Ctrl (Windows) or Cmd (Mac) to select multiple files
          </small>
        </div>

        {files.length > 0 && (
          <div className="mb-4 p-4 bg-light rounded border">
            <h5 className="text-success" style={{ fontSize: "14px"}}>
              {files.length} file(s) selected → Will create {files.length}{" "}
              records:
            </h5>
            {files.map((file, i) => (
              <div key={i} className="border p-3 my-2 rounded bg-white" style={{ fontSize: "14px"}}>
                <strong>Title:</strong> {file.name.replace(/\.[^/.]+$/, "")}
                <br />
                <strong>Description:</strong> {file.name}
                <br />
                <span className="badge bg-primary">
                  {(file.size / 1024 / 1024).toFixed(2)} MB
                </span>
              </div>
            ))}
          </div>
        )}

        <div className="text-center" style={{ fontSize: "14px !important" }}>
          <Buton
            title={`Upload ${files.length} Files Now`}
            disabled={files.length === 0}
          />
        </div>
      </form>
    </div>
  );
}

export default Form;
