import { useState } from "react";

const Search = () => {
    const [username, setUsername] = useState("");
    const [parameters, setParameters] = useState({
        json: true,
        no_progress: true,
        timeout: 5,
        site: "",
        tags: "",
    });

    const handleSearch = async () => {
        const queryParams = new URLSearchParams({
            username,
            json: parameters.json,
            no_progress: parameters.no_progress,
            timeout: parameters.timeout,
            site: parameters.site,
            tags: parameters.tags,
        }).toString();

        const response = await fetch(`http://localhost:8000/search?${queryParams}`);
        const data = await response.json();
        setResult(data.output);
    };

    return (
        <div>
            <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
                placeholder="Enter username"
            />

            <label>
                Timeout (seconds):
                <input
                    type="number"
                    value={parameters.timeout}
                    onChange={(e) => setParameters({ ...parameters, timeout: e.target.value })}
                />
            </label>

            <label>
                Specific Site (comma-separated):
                <input
                    type="text"
                    value={parameters.site}
                    onChange={(e) => setParameters({ ...parameters, site: e.target.value })}
                />
            </label>

            <label>
                Tags (comma-separated):
                <input
                    type="text"
                    value={parameters.tags}
                    onChange={(e) => setParameters({ ...parameters, tags: e.target.value })}
                />
            </label>

            <button onClick={handleSearch}>Search</button>

            {result && <pre>{JSON.stringify(result, null, 2)}</pre>}
        </div>
    );
};

export default Search;
