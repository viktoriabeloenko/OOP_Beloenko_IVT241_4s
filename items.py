from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import Item as ItemModel, TodoList as TodoListModel
from schemas import ItemCreate, ItemUpdate, ItemResponse

def init_routes(app):
    
    @app.get("/items", response_model=list[ItemResponse])
    def get_all(db: Session = Depends(get_db)):
        return db.query(ItemModel).all()
    
    @app.get("/items/{id}", response_model=ItemResponse)
    def get_one(id: int, db: Session = Depends(get_db)):
        item = db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(404, "Элемент не найден")
        return item
    
    @app.get("/todo-lists/{list_id}/items", response_model=list[ItemResponse])
    def get_by_list(list_id: int, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == list_id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        return db.query(ItemModel).filter(ItemModel.todo_list_id == list_id).all()
    
    @app.post("/todo-lists/{list_id}/items", response_model=ItemResponse, status_code=201)
    def create(list_id: int, data: ItemCreate, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == list_id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        new_item = ItemModel(
            name=data.name,
            text=data.text,
            is_done=data.is_done,
            todo_list_id=list_id
        )
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item
    
    @app.put("/items/{id}", response_model=ItemResponse)
    def update(id: int, data: ItemUpdate, db: Session = Depends(get_db)):
        item = db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(404, "Элемент не найден")
        if data.name is not None:
            item.name = data.name
        if data.text is not None:
            item.text = data.text
        if data.is_done is not None:
            item.is_done = data.is_done
        db.commit()
        db.refresh(item)
        return item
    
    @app.delete("/items/{id}")
    def delete(id: int, db: Session = Depends(get_db)):
        item = db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(404, "Элемент не найден")
        db.delete(item)
        db.commit()
        return {"message": "Элемент удален"}