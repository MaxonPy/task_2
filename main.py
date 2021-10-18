import uvicorn
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()
m = []
@app.get("/")
def Root():
    return "Hello World"


@app.get("/api/products") # список товаров
def watch_all_products():
    global m
    return m

@app.get("/api/products/{id}") # информация о товаре по id
def watch_current_product(id: int):
    global m
    for i in range(len(m)):
        if m[i]["id"] == id:
            return m[i]
    return "Данный товар отсутствует"

@app.post("/api/products/new") # создание нового товара
def create_new_product(id: int, name: str, description: str, prise:float):
    global m
    mgl = {
        "id": id,
        "name": name,
        "description": description,
        "prise": prise
    }
    m.append(mgl)
    return m

@app.put("/api/products/edit/{id}") # обновление информации о товаре
def edit_product(id: int, name: str, description: str, prise:float):
    global m
    for i in range(len(m)):
        if m[i]["id"] == id:
            m[i]["name"] = name
            m[i]["description"] = description
            m[i]["prise"] = prise
            return m[i]
    return "Данный товар отсутствует"

@app.delete("/api/products/delete/{id}") # удаление товара
def delete_product(id: int):
    global m
    for i in range(len(m)):
        if m[i]["id"] == id:
            del m[i]
            return "ok"
    return "Данный товар отсутствует"

if __name__ == '__main__':
    uvicorn.run(app, host = "127.0.0.1", port=8000)