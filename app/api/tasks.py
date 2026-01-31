from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class Task(BaseModel):
    id: Optional[int] = None
    project_id: int
    title: str
    description: str
    status: str = "pending"
    priority: str = "medium"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Mock data
tasks_db = [
    {"id": 1, "project_id": 1, "title": "Tarea 1", "description": "Primera tarea", "status": "pending", "priority": "high"},
    {"id": 2, "project_id": 1, "title": "Tarea 2", "description": "Segunda tarea", "status": "in_progress", "priority": "medium"},
    {"id": 3, "project_id": 2, "title": "Tarea 3", "description": "Tercera tarea", "status": "completed", "priority": "low"},
]

@router.get("/", response_model=List[Task])
async def list_tasks(project_id: Optional[int] = None):
    """Listar tareas, opcionalmente filtradas por proyecto"""
    if project_id:
        return [t for t in tasks_db if t["project_id"] == project_id]
    return tasks_db

@router.get("/{task_id}", response_model=Task)
async def get_task(task_id: int):
    """Obtener una tarea específica"""
    for task in tasks_db:
        if task["id"] == task_id:
            return task
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.post("/", response_model=Task)
async def create_task(task: Task):
    """Crear una nueva tarea"""
    new_id = max([t["id"] for t in tasks_db]) + 1 if tasks_db else 1
    new_task = {
        "id": new_id,
        "project_id": task.project_id,
        "title": task.title,
        "description": task.description,
        "status": task.status,
        "priority": task.priority,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    tasks_db.append(new_task)
    return new_task

@router.put("/{task_id}", response_model=Task)
async def update_task(task_id: int, task: Task):
    """Actualizar una tarea"""
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            tasks_db[i] = {
                **t,
                "title": task.title,
                "description": task.description,
                "status": task.status,
                "priority": task.priority,
                "updated_at": datetime.now(),
            }
            return tasks_db[i]
    raise HTTPException(status_code=404, detail="Tarea no encontrada")

@router.delete("/{task_id}")
async def delete_task(task_id: int):
    """Eliminar una tarea"""
    for i, t in enumerate(tasks_db):
        if t["id"] == task_id:
            deleted = tasks_db.pop(i)
            return {"message": "Tarea eliminada", "task": deleted}
    raise HTTPException(status_code=404, detail="Tarea no encontrada")
