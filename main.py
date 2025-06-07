from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Define the Item model that clients will use to send data
class Item(BaseModel):
    text: str   #required
    is_done: bool = False

# Root endpoint to verify the app is running
@app.get("/")
def root():
    return {"status": "running", "message": "FastAPI is alive"}