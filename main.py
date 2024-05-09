from fastapi import FastAPI

app = FastAPI()

items = [
  {"name": "Foo"},
  {"name": "Bar"},
  {"name": "Baz"}
]

@app.get("/items")
async def read_items(skip: int = 0, limit: int = 10):
  return items[skip: skip+limit]

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str | None = None, short: bool = False):
  item = {"item_id": item_id}
  if q:
    item.update({"q": q})

  if not short:
    item.update({"description": "This is an amazing item that has a long description"})

  return item
