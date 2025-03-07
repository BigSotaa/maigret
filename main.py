# filepath: /Users/andrewbulthuis/vscode/maigret/main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow all origins (for development purposes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "FastAPI is running!"}

@app.get("/search")
def search_user(username: str, json: bool = True, no_progress: bool = True, timeout: int = 5, site: str = "", tags: str = ""):
    # Your search logic here
    return {"searched_username": username}
