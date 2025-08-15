import React, { useState } from "react";
import api from "../api";

const Login: React.FC<{ onLogin: (token: string) => void }> = ({ onLogin }) => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [err, setErr] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setErr("");
    try {
      const res = await api.post("/login", { username, password });
      onLogin(res.data.token);
    } catch {
      setErr("Login failed (any username/password works for demo)");
    }
  };

  return (
    <form onSubmit={submit} style={{ maxWidth: 400, margin: "100px auto" }}>
      <h2>Login</h2>
      {err && <div style={{ color: "red" }}>{err}</div>}
      <input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        required
        style={{ width: "100%", margin: 8 }}
      />
      <input
        placeholder="Password"
        type="password"
        value={password}
        required
        onChange={(e) => setPassword(e.target.value)}
        style={{ width: "100%", margin: 8 }}
      />
      <button type="submit" style={{ width: "100%" }}>
        Login
      </button>
    </form>
  );
};
export default Login;
