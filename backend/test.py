from fastapi import FastAPI
import models

app = FastAPI()


@app.post("/items/")
async def create_item(item: models.Item):
    return item.name
