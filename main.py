from fastapi import FastAPI
import uvicorn

from database import Base, engine
from todo_lists import init_routes as init_todo_routes
from items import init_routes as init_items_routes

# Создаём таблицы
Base.metadata.create_all(bind=engine)

def bootstrap(app: FastAPI):
    init_todo_routes(app)
    init_items_routes(app)

if __name__ == "__main__":
    app = FastAPI(title="Todo List API with Progress")
    bootstrap(app)
    uvicorn.run(app, host="127.0.0.1", port=8000)
