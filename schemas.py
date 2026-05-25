from pydantic import BaseModel
from typing import Optional

class TodoListCreate(BaseModel):
    name: str

class TodoListUpdate(BaseModel):
    name: Optional[str] = None

class TodoListResponse(BaseModel):
    id: int
    name: str

class ItemCreate(BaseModel):
    name: str
    text: Optional[str] = None
    is_done: bool = False

class ItemUpdate(BaseModel):
    name: Optional[str] = None
    text: Optional[str] = None
    is_done: Optional[bool] = None

class ItemResponse(BaseModel):
    id: int
    name: str
    text: Optional[str]
    is_done: bool
    todo_list_id: int