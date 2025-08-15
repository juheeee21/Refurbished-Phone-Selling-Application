import React, { useRef, useState } from "react";
import api from "../api";

const BulkUpload: React.FC<{ onUpload: () => void }> = ({ onUpload }) => {
  const fileRef = useRef<HTMLInputElement>(null);
  const [err, setErr] = useState("");
  const [msg, setMsg] = useState("");

  const handleUpload = async (e: React.FormEvent) => {
    e.preventDefault();
    setErr("");
    setMsg("");
    if (!fileRef.current || !fileRef.current.files) return;
    const form = new FormData();
    form.append("file", fileRef.current.files[0]);
    try {
      await api.post("/phones/bulk_upload", form, {
        headers: { "Content-Type": "multipart/form-data" },
      });
      setMsg("Upload successful");
      onUpload();
    } catch {
      setErr("Upload failed. Check CSV format.");
    }
  };

  return (
    <form onSubmit={handleUpload} style={{ margin: "16px 0" }}>
      <input type="file" ref={fileRef} accept=".csv" required />
      <button type="submit">Bulk Upload CSV</button>
      {msg && <span style={{ color: "green", marginLeft: 8 }}>{msg}</span>}
      {err && <span style={{ color: "red", marginLeft: 8 }}>{err}</span>}
    </form>
  );
};
export default BulkUpload;
