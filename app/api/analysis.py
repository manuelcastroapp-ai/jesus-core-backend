from fastapi import APIRouter
from pydantic import BaseModel
from typing import List, Dict, Any

router = APIRouter()

class AnalysisReport(BaseModel):
    project_id: int
    total_tasks: int
    completed_tasks: int
    completion_rate: float
    avg_priority: str
    status: str

@router.get("/project/{project_id}", response_model=AnalysisReport)
async def analyze_project(project_id: int):
    """Analizar un proyecto específico"""
    # Mock analysis data
    return {
        "project_id": project_id,
        "total_tasks": 15,
        "completed_tasks": 8,
        "completion_rate": 53.3,
        "avg_priority": "medium",
        "status": "on_track"
    }

@router.get("/dashboard")
async def dashboard_analytics():
    """Obtener análisis del dashboard"""
    return {
        "total_projects": 102,
        "active_projects": 101,
        "completed_projects": 1,
        "total_tasks": 245,
        "completed_tasks": 89,
        "completion_rate": 36.3,
        "team_members": 12,
        "recent_activity": [
            {"type": "project_created", "name": "Proyecto Alpha", "timestamp": "2024-01-30T10:00:00"},
            {"type": "task_completed", "name": "Tarea 1", "timestamp": "2024-01-30T09:30:00"},
            {"type": "team_joined", "name": "Juan Pérez", "timestamp": "2024-01-30T09:00:00"},
        ]
    }

@router.get("/trends")
async def get_trends():
    """Obtener tendencias del sistema"""
    return {
        "weekly_completion": [12, 15, 18, 14, 16, 19, 21],
        "project_distribution": {
            "active": 101,
            "completed": 1,
            "on_hold": 0
        },
        "priority_distribution": {
            "high": 45,
            "medium": 120,
            "low": 80
        }
    }
