from fastapi import HTTPException, Depends
from sqlalchemy.orm import Session
from database import get_db
from models import TodoList as TodoListModel
from schemas import TodoListCreate, TodoListUpdate, TodoListResponse

def init_routes(app):
    
    @app.get("/todo-lists", response_model=list[TodoListResponse])
    def get_all(db: Session = Depends(get_db)):
        todo_lists = db.query(TodoListModel).all()
        result = []
        for tl in todo_lists:
            progress = 0
            if tl.total_items > 0:
                progress = round(tl.completed_items / tl.total_items * 100, 2)
            result.append(TodoListResponse(id=tl.id, name=tl.name, progress=progress))
        return result
    
    @app.get("/todo-lists/{id}", response_model=TodoListResponse)
    def get_one(id: int, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        progress = 0
        if todo_list.total_items > 0:
            progress = round(todo_list.completed_items / todo_list.total_items * 100, 2)
        return TodoListResponse(id=todo_list.id, name=todo_list.name, progress=progress)
    
    @app.post("/todo-lists", response_model=TodoListResponse, status_code=201)
    def create(data: TodoListCreate, db: Session = Depends(get_db)):
        new_list = TodoListModel(name=data.name, total_items=0, completed_items=0)
        db.add(new_list)
        db.commit()
        db.refresh(new_list)
        return TodoListResponse(id=new_list.id, name=new_list.name, progress=0)
    
    @app.put("/todo-lists/{id}", response_model=TodoListResponse)
    def update(id: int, data: TodoListUpdate, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        if data.name is not None:
            todo_list.name = data.name
        db.commit()
        db.refresh(todo_list)
        progress = 0
        if todo_list.total_items > 0:
            progress = round(todo_list.completed_items / todo_list.total_items * 100, 2)
        return TodoListResponse(id=todo_list.id, name=todo_list.name, progress=progress)
    
    @app.delete("/todo-lists/{id}")
    def delete(id: int, db: Session = Depends(get_db)):
        todo_list = db.query(TodoListModel).filter(TodoListModel.id == id).first()
        if not todo_list:
            raise HTTPException(404, "Список не найден")
        db.delete(todo_list)
        db.commit()
        return {"message": "Список удален"}