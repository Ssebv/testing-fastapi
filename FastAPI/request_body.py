from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool = None
    tax: float = None

app = FastAPI()

items = [] # Lista para almacenar los objetos 'item'.




@app.post("/items/")
async def create_item(item: Item):
    items.append(item.dict())  # Guardamos el objeto 'item' en la lista.
    if item.tax:
        price_with_tax = item.price + item.tax
        return {"price_with_tax": price_with_tax}
    return item.dict()

@app.get("/items/")
async def read_items():
    return items  # Retornamos todos los objetos 'item'.