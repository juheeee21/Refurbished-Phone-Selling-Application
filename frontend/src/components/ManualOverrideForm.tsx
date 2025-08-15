import React, { useState } from "react";
import api from "../api";
import { Phone, ManualOverride } from "../types";

const ManualOverrideForm: React.FC<{ phone: Phone; onOverride: () => void }> = ({
  phone,
  onOverride,
}) => {
  const [overrides, setOverrides] = useState<ManualOverride>({});
  const [msg, setMsg] = useState("");

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    setMsg("");
    try {
      await api.post(`/phones/${phone.id}/manual_override`, overrides);
      setMsg("Override updated!");
      onOverride();
    } catch {
      setMsg("Override failed");
    }
  };

  return (
    <form onSubmit={submit} style={{ margin: "12px 0" }}>
      <h3>Manual Price Override</h3>
      <div>
        {["X", "Y", "Z"].map((plat) => (
          <span key={plat} style={{ marginRight: 12 }}>
            {plat}:{" "}
            <input
              type="number"
              step="0.01"
              value={overrides[plat as "X" | "Y" | "Z"] ?? ""}
              onChange={(e) =>
                setOverrides((curr) => ({
                  ...curr,
                  [plat]: e.target.value ? Number(e.target.value) : undefined,
                }))
              }
              style={{ width: 70 }}
            />
          </span>
        ))}
        <button type="submit">Set Override</button>
        {msg && <span style={{ marginLeft: 8 }}>{msg}</span>}
      </div>
    </form>
  );
};
export default ManualOverrideForm;
