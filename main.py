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

items = []
#Create a new to-do item and add it to the list
@app.post("/items")
def creat_item(item: Item):
    items.append(item)
    return items