from fastapi import FastAPI, HTTPException,status
from pydantic import BaseModel
from database import Sessionlocal
import uvicorn
from models import Item


app=FastAPI()


db = Sessionlocal()

class ItemCreate(BaseModel):
    title:str
    description:str
    price:int

    class config:
        orm_mode=True


@app.get('/items',status_code=status.HTTP_200_OK)
def get_all_items():
    items = db.query(Item).all()
    return items

@app.get('/item/{item_id}',status_code=status.HTTP_200_OK)
def get_item(item_id:int):
    item = db.query(Item).filter(Item.id == item_id).first()
    return item

@app.post('/item',status_code=status.HTTP_201_CREATED)
def create_item(item:ItemCreate):
    new_item = Item(
        title=item.title,
        description=item.description,
        price = item.price
    )

    db_item = db.query(Item).filter(Item.title == new_item.title).first()

    if db_item is not None:
        raise HTTPException(status_code=400,detail="Item already exists")

    db.add(new_item)
    db.commit()
    return "Data Added Successfully"

@app.put('/update/{item_id}')
def update_item(item_id:int,item:ItemCreate):
    update_item = db.query(Item).filter(Item.id == item_id).first()
    update_item.title = item.title
    update_item.description = item.description
    update_item.price = item.price

    db.commit()
    db.refresh(update_item)

    return "Item updated successfully"

@app.delete('/delete/{item_id}')
def delete_item(item_id:int):
    delete_item = db.query(Item).filter(Item.id == item_id).first()

    if delete_item is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Item not found")
    
    db.delete(delete_item)
    db.commit()

    return "delete item"


if __name__ == "__main__":
    uvicorn.run("main:app",host="127.0.0.1",port=8000,reload=True)