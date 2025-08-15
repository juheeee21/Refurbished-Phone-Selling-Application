import React, { useState } from "react";
import api from "../api";
import { Phone, ListingResult } from "../types";

const platforms = ["X", "Y", "Z"];

const ListingSimulator: React.FC<{ phone: Phone }> = ({ phone }) => {
  const [platform, setPlatform] = useState("X");
  const [result, setResult] = useState<ListingResult | null>(null);

  const simulate = async () => {
    setResult(null);
    try {
      const res = await api.post(`/phones/${phone.id}/list/${platform}`);
      setResult(res.data);
    } catch {
      setResult({ success: false, error: "Simulate failed" });
    }
  };

  return (
    <div style={{ margin: "16px 0", border: "1px solid #aaa", padding: 12 }}>
      <h3>Simulate Platform Listing</h3>
      <select value={platform} onChange={(e) => setPlatform(e.target.value)}>
        {platforms.map((p) => (
          <option key={p}>{p}</option>
        ))}
      </select>
      <button onClick={simulate} style={{ marginLeft: 8 }}>Simulate Listing</button>
      {result && (
        <div style={{ marginTop: 8 }}>
          {result.success ? (
            <span>
              Success! Listed on {result.platform} at ${result.price} ({result.mapped_condition})
            </span>
          ) : (
            <span style={{ color: "red" }}>Failed: {result.error}</span>
          )}
        </div>
      )}
    </div>
  );
};
export default ListingSimulator;
