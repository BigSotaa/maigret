import React, { useState } from "react";

function App() {
  const [username, setUsername] = useState("");
  const [options, setOptions] = useState({
    parseUrl: "",
    tags: [],
    maxConnections: 100,
    allSites: false,
    topSites: 500,
    timeout: 30,
    cookiesFile: null,
    noRecursion: false,
    useDisabledSites: false,
    idType: "gaia_id",
    ignoreIds: "",
    databaseFile: null,
    retries: 3,
    reports: {
      pdf: false,
      html: false,
      xmind: false,
      csv: false,
      txt: false,
      json: "simple",
    },
    output: {
      verbose: false,
      info: false,
      debug: false,
      printNotFound: false,
      printErrors: false,
    },
  });

  const handleSearch = async () => {
    const formData = new FormData();
    formData.append("username", username);
    formData.append("options", JSON.stringify(options));

    if (options.cookiesFile) {
      formData.append("cookiesFile", options.cookiesFile);
    }
    if (options.databaseFile) {
      formData.append("databaseFile", options.databaseFile);
    }

    const response = await fetch("http://localhost:8000/run", {
      method: "POST",
      body: formData,
    });

    const data = await response.json();
    console.log("Search Results:", data);
  };

  return (
    <div style={{ padding: "20px", fontFamily: "Arial, sans-serif" }}>
      <h1>Maigret Interactive Web App</h1>

      <input
        type="text"
        placeholder="Enter Username(s)"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        style={{ width: "300px", padding: "10px", marginBottom: "10px" }}
      />

      <br />

      <label>Parse URL:</label>
      <input
        type="text"
        placeholder="Profile URL"
        value={options.parseUrl}
        onChange={(e) => setOptions({ ...options, parseUrl: e.target.value })}
      />

      <br />

      <label>Max Connections:</label>
      <input
        type="number"
        value={options.maxConnections}
        onChange={(e) => setOptions({ ...options, maxConnections: e.target.value })}
      />

      <br />

      <label>Top Sites:</label>
      <input
        type="number"
        value={options.topSites}
        onChange={(e) => setOptions({ ...options, topSites: e.target.value })}
      />

      <br />

      <label>Timeout:</label>
      <input
        type="number"
        value={options.timeout}
        onChange={(e) => setOptions({ ...options, timeout: e.target.value })}
      />

      <br />

      <label>Identifier Type:</label>
      <select
        value={options.idType}
        onChange={(e) => setOptions({ ...options, idType: e.target.value })}
      >
        <option value="gaia_id">Gaia ID</option>
        <option value="vk_id">VK ID</option>
        <option value="yandex_public_id">Yandex Public ID</option>
        <option value="ok_id">OK ID</option>
        <option value="wikimapia_uid">Wikimapia UID</option>
      </select>

      <br />

      <button
        onClick={handleSearch}
        style={{ backgroundColor: "#007bff", color: "white", padding: "10px", marginTop: "10px" }}
      >
        RUN MAIGRET
      </button>
    </div>
  );
}

export default App;
