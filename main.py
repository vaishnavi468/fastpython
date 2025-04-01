from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load student marks from marks.json
with open("q-vercel-python.json", "r") as file:
    marks_data = {student["name"]: student["marks"] for student in json.load(file)}

@app.get("/api")
def get_marks(name: list[str] = Query(...)):
    result = [marks_data.get(n, 0) for n in name]  # Default to 0 if name not found
    return {"marks": result}
