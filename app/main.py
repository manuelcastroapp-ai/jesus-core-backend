from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

# Importar routers
from app.api import projects, tasks, analysis, modules

# Lifespan context manager
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    print("🚀 JESUS CORE Backend iniciado")
    yield
    # Shutdown
    print("🛑 JESUS CORE Backend detenido")

# Crear aplicación FastAPI
app = FastAPI(
    title="JESUS CORE API",
    description="Plataforma Científica de Gestión de Proyectos",
    version="1.0.0",
    lifespan=lifespan
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(projects.router, prefix="/api/projects", tags=["Projects"])
app.include_router(tasks.router, prefix="/api/tasks", tags=["Tasks"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["Analysis"])
app.include_router(modules.router, prefix="/api/modules", tags=["Modules"])

# Health check
@app.get("/api/health")
async def health_check():
    return {
        "status": "healthy",
        "service": "JESUS CORE API",
        "version": "1.0.0"
    }

# Root endpoint
@app.get("/")
async def root():
    return {
        "message": "JESUS CORE API",
        "version": "1.0.0",
        "docs": "/docs"
    }

if __name__ == "__main__":
    import uvicorn
    import os

    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)

