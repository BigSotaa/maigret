const API_URL = "http://localhost:8000"; // Change this if your backend is hosted elsewhere

export async function runMaigret(username, options) {
    try {
        const response = await fetch(`${API_URL}/run`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ username, options }),
        });

        if (!response.ok) {
            throw new Error(`Error: ${response.statusText}`);
        }

        const data = await response.json();
        return data;
    } catch (error) {
        console.error("Failed to run Maigret:", error);
        return { error: "Failed to fetch results" };
    }
}
