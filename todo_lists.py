from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import TodoList as TodoListModel
from schemas import TodoListCreate, TodoListUpdate, TodoListResponse

def init_routes(app):
    
    @app.get("/todo-lists", response_model=list[TodoListResponse])
    def get_all(db: Session = Depends(get_db)):
        return db.query(TodoListModel).all()
    
    @app.get("/todo-lists/{id}", response_model=TodoListResponse)
    def get_one(id: int, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        return todo_list
    
    @app.post("/todo-lists", response_model=TodoListResponse, status_code=201)
    def create(data: TodoListCreate, db: Session = Depends(get_db)):
        new_list = TodoListModel(name=data.name)
        db.add(new_list)
        db.commit()
        db.refresh(new_list)
        return new_list
    
    @app.put("/todo-lists/{id}", response_model=TodoListResponse)
    def update(id: int, data: TodoListUpdate, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        if data.name is not None:
            todo_list.name = data.name
        db.commit()
        db.refresh(todo_list)
        return todo_list
    
    @app.delete("/todo-lists/{id}")
    def delete(id: int, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        db.delete(todo_list)
        db.commit()
        return {"message": "Список удален"}