from fastapi import FastAPI, Query
import subprocess

app = FastAPI()

@app.get("/search")
def search_user(
    username: str,
    json: bool = Query(True),
    no_progress: bool = Query(True),
    timeout: int = Query(5),
    site: str = Query("", description="Comma-separated sites"),
    tags: str = Query("", description="Comma-separated tags")
):
    command = ["python", "-m", "maigret", username]

    # Add optional parameters
    if json:
        command.append("--json")
    if no_progress:
        command.append("--no-progress")
    if timeout:
        command.extend(["--timeout", str(timeout)])
    if site:
        command.extend(["--site", site])
    if tags:
        command.extend(["--tags", tags])

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return {"output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
