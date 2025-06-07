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

# List the to-do items, with optional limit
@app.get("/items", response_model = list[Item])
def list_items(limit: int = 10):
    return items[0:limit]

#view certain item
@app.get("/items/{item_id}", response_model = Item)
def get_item(item_id: int) -> Item:
    if item_id < len(items):
        return items[item_id]
    else:
        raise HTTPException(status_code = 404, detail = f"Item {item_id} not found")