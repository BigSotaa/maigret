from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import subprocess

app = FastAPI()

# CORS Middleware to allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this for security in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "Maigret API is running"}

@app.post("/run")
def run_maigret(data: dict):
    username = data.get("username", "")
    options = data.get("options", {})

    command = ["maigret", username]

    for key, value in options.items():
        if isinstance(value, bool) and value:
            command.append(f"--{key}")
        elif value:
            command.append(f"--{key}")
            command.append(str(value))

    try:
        result = subprocess.run(command, capture_output=True, text=True)
        return {"command": " ".join(command), "output": result.stdout}
    except Exception as e:
        return {"error": str(e)}
