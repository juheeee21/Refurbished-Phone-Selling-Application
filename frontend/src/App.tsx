import React, { useState, useEffect } from "react";
import api, { setAuthToken } from "./api";
import { Phone, ListingResult, ManualOverride } from "./types";
import Login from "./components/Login";
import Inventory from "./components/Inventory";
import BulkUpload from "./components/BulkUpload";
import ListingSimulator from "./components/ListingSimulator";
import ManualOverrideForm from "./components/ManualOverrideForm";

function App() {
  const [token, setToken] = useState<string | null>(null);
  const [phones, setPhones] = useState<Phone[]>([]);
  const [selectedPhone, setSelectedPhone] = useState<Phone | null>(null);
  const [refresh, setRefresh] = useState(0);

  useEffect(() => {
    if (token) {
      setAuthToken(token);
      fetchPhones();
    }
  }, [token, refresh]);

  const fetchPhones = async () => {
    const res = await api.get<Phone[]>("/phones/");
    setPhones(res.data);
  };

  if (!token) return <Login onLogin={setToken} />;

  return (
    <div style={{ maxWidth: 900, margin: "0 auto", padding: 24 }}>
      <h1>Refurbished Phone Inventory</h1>
      <button onClick={() => setToken(null)}>Logout</button>
      <BulkUpload onUpload={() => setRefresh((r) => r + 1)} />
      <Inventory
        phones={phones}
        setSelectedPhone={setSelectedPhone}
        setRefresh={() => setRefresh((r) => r + 1)}
      />
      {selectedPhone && (
        <>
          <ListingSimulator phone={selectedPhone} />
          <ManualOverrideForm
            phone={selectedPhone}
            onOverride={() => setRefresh((r) => r + 1)}
          />
        </>
      )}
    </div>
  );
}

export default App;
