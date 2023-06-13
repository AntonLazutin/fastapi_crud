from fastapi import FastAPI
import uvicorn
import pydantic


app = FastAPI()


class Item(pydantic.BaseModel):
    id: int
    name: str
    price: float
    description: str = "new item"


@app.get('/')
async def index(item_id: int = 0):
    return {"status": "ok"}


@app.post('/items')
async def create_item(item: Item):
    item.__dict__["description"] = f"this is {item.name}"
    return item.dict()


@app.get('/{item_id}')
async def get_id(item_id: int = 0, arg1: int = 0, arg2: int = 0):
    return {"item_id": item_id, "arg1": arg1, "arg2":arg2}


if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=8000, reload=True, workers=3)