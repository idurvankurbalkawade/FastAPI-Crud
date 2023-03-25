from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from typing import Optional
from database import Sessionlocal
import uvicorn
import models


app=FastAPI()


db = Sessionlocal()

class ItemCreate(BaseModel):
    title:str
    description:str

    class config:
        orm_mode=True


@app.get('/items')
def get_all_items():
    items = db.query(models.Item).all()
    return items

@app.get('/item/{item_id}')
def get_item(item_id:int):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    return item

@app.post('/item')
def create_item(item:ItemCreate):
    new_item = models.Item(
        title=item.title,
        description=item.description
    )

    db.add(new_item)
    db.commit()
    return "Data Added Successfully"

@app.put('/update/{item_id}')
def update_item(item_id:int,item:ItemCreate):
    update_item = db.query(models.Item).filter(models.Item.id == item_id).first()
    update_item.title = item.title
    update_item.description = item.description

    db.commit()

    return "Item updated successfully"

@app.delete('/delete/{item_id}')
def delete_item(item_id:int):
    delete_item = db.query(models.Item).filter(models.Item.id == item_id).first()

    if delete_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")
    
    db.delete(delete_item)
    db.commit()

    return "delete item"


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)