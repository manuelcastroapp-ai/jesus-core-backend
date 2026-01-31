from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

router = APIRouter()

class Project(BaseModel):
    id: Optional[int] = None
    name: str
    description: str
    status: str = "active"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

# Mock data
projects_db = [
    {"id": 1, "name": "Proyecto Alpha", "description": "Investigación inicial", "status": "active"},
    {"id": 2, "name": "Proyecto Beta", "description": "Fase de desarrollo", "status": "active"},
    {"id": 3, "name": "Proyecto Gamma", "description": "Análisis de resultados", "status": "completed"},
]

@router.get("/", response_model=List[Project])
async def list_projects():
    """Listar todos los proyectos"""
    return projects_db

@router.get("/{project_id}", response_model=Project)
async def get_project(project_id: int):
    """Obtener un proyecto específico"""
    for project in projects_db:
        if project["id"] == project_id:
            return project
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@router.post("/", response_model=Project)
async def create_project(project: Project):
    """Crear un nuevo proyecto"""
    new_id = max([p["id"] for p in projects_db]) + 1 if projects_db else 1
    new_project = {
        "id": new_id,
        "name": project.name,
        "description": project.description,
        "status": project.status,
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
    }
    projects_db.append(new_project)
    return new_project

@router.put("/{project_id}", response_model=Project)
async def update_project(project_id: int, project: Project):
    """Actualizar un proyecto"""
    for i, p in enumerate(projects_db):
        if p["id"] == project_id:
            projects_db[i] = {
                **p,
                "name": project.name,
                "description": project.description,
                "status": project.status,
                "updated_at": datetime.now(),
            }
            return projects_db[i]
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")

@router.delete("/{project_id}")
async def delete_project(project_id: int):
    """Eliminar un proyecto"""
    for i, p in enumerate(projects_db):
        if p["id"] == project_id:
            deleted = projects_db.pop(i)
            return {"message": "Proyecto eliminado", "project": deleted}
    raise HTTPException(status_code=404, detail="Proyecto no encontrado")
