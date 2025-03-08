from fastapi import FastAPI, Query
import subprocess
import json

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Maigret API is running!"}

@app.get("/search")
def search_user(
    username: str,
    json_output: bool = Query(True, description="Return results in JSON format"),
    no_progress: bool = Query(True, description="Disable progress bar"),
    timeout: int = Query(10, description="Request timeout in seconds"),
    site: str = Query("", description="Comma-separated list of specific sites to search"),
    tags: str = Query("", description="Comma-separated tags to filter sites"),
    output_file: str = Query("", description="Save results to a specific file")
):
    # Construct the command dynamically
    command = ["python", "-m", "maigret", username]

    if json_output:
        command.append("--json")
    if no_progress:
        command.append("--no-progress")
    if timeout:
        command.extend(["--timeout", str(timeout)])
    if site:
        command.extend(["--site", site])
    if tags:
        command.extend(["--tags", tags])
    if output_file:
        command.extend(["--output", output_file])

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return {"command": " ".join(command), "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
