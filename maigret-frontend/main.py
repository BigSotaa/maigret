from fastapi import FastAPI, Form, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional
import json
import subprocess

app = FastAPI()

# CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Adjust for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/run")
async def run_maigret(
    username: str = Form(...),
    options: str = Form(...),
    cookiesFile: Optional[UploadFile] = File(None),
    databaseFile: Optional[UploadFile] = File(None),
):
    options_dict = json.loads(options)

    # Prepare Maigret command
    command = ["maigret", username]

    # Add options dynamically
    if options_dict.get("all_sites"):
        command.append("-a")
    if options_dict.get("top_sites"):
        command.extend(["--top-sites", str(options_dict["top_sites"])])
    if options_dict.get("timeout"):
        command.extend(["--timeout", str(options_dict["timeout"])])
    if options_dict.get("verbose"):
        command.append("-v")
    if options_dict.get("info"):
        command.append("-vv")
    if options_dict.get("debug"):
        command.append("-vvv")
    if options_dict.get("pdf_report"):
        command.append("-P")
    if options_dict.get("html_report"):
        command.append("-H")
    if options_dict.get("csv_report"):
        command.append("-C")

    # Run Maigret process
    try:
        result = subprocess.run(command, capture_output=True, text=True)
        output = result.stdout
    except Exception as e:
        output = str(e)

    return {
        "username": username,
        "options": options_dict,
        "output": output,
    }
