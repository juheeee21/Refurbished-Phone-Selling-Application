import React, { useState } from "react";
import api from "../api";
import { Phone } from "../types";

type Props = {
  phones: Phone[];
  setSelectedPhone: (p: Phone | null) => void;
  setRefresh: () => void;
};

const Inventory: React.FC<Props> = ({ phones, setSelectedPhone, setRefresh }) => {
  const [search, setSearch] = useState("");
  const [condition, setCondition] = useState("");
  const [platform, setPlatform] = useState("");

  const filtered = phones.filter(
    (p) =>
      (!search ||
        p.model.toLowerCase().includes(search.toLowerCase()) ||
        p.brand.toLowerCase().includes(search.toLowerCase())) &&
      (!condition || p.condition === condition)
  );

  const deletePhone = async (id: number) => {
    if (window.confirm("Delete this phone?")) {
      await api.delete(`/phones/${id}`);
      setRefresh();
    }
  };

  return (
    <div>
      <h2>Inventory</h2>
      <input
        placeholder="Search model or brand"
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{ margin: 4 }}
      />
      <select value={condition} onChange={(e) => setCondition(e.target.value)} style={{ margin: 4 }}>
        <option value="">All Conditions</option>
        <option>New</option>
        <option>Good</option>
        <option>Scrap</option>
      </select>
      <table border={1} cellPadding={6} style={{ width: "100%", marginTop: 8 }}>
        <thead>
          <tr>
            <th>Brand</th>
            <th>Model</th>
            <th>Condition</th>
            <th>Specs</th>
            <th>Stock</th>
            <th>Base Price</th>
            <th>Tags</th>
            <th>Manual Overrides</th>
            <th>Actions</th>
          </tr>
        </thead>
        <tbody>
          {filtered.map((p) => (
            <tr key={p.id} style={{ background: p.stock <= 0 ? "#fdd" : undefined }}>
              <td>{p.brand}</td>
              <td>{p.model}</td>
              <td>{p.condition}</td>
              <td>
                {Object.entries(p.specs)
                  .map(([k, v]) => `${k}: ${v}`)
                  .join(", ")}
              </td>
              <td>{p.stock}</td>
              <td>${p.base_price}</td>
              <td>{p.tags.join(", ")}</td>
              <td>
                {p.manual_price_overrides &&
                  Object.entries(p.manual_price_overrides)
                    .map(([plat, price]) => `${plat}: $${price}`)
                    .join(", ")}
              </td>
              <td>
                <button onClick={() => setSelectedPhone(p)}>Details</button>
                <button onClick={() => deletePhone(p.id)}>Delete</button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};
export default Inventory;
