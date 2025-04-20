from fastapi import FastAPI
from app.routes import (Components, ConceptBoards, Concepts, Permissions, Priorities,
                        Projects, ProjectUsers, Roles, TaskBoards, TaskDependencies,
                        TaskProgress, Tasks, TaskSections, Types, UserProjectPermissions, Users)
from app.db.session import engine, fill_base_data
from sqlmodel import SQLModel

app = FastAPI()

# Registrar las rutas
app.include_router(Components.router)
app.include_router(ConceptBoards.router)
app.include_router(Concepts.router)
app.include_router(Permissions.router)
app.include_router(Priorities.router)
app.include_router(Projects.router)
app.include_router(ProjectUsers.router)
app.include_router(Roles.router)
app.include_router(TaskBoards.router)
app.include_router(TaskDependencies.router)
app.include_router(TaskProgress.router)
app.include_router(Tasks.router)
app.include_router(TaskSections.router)
app.include_router(Types.router)
app.include_router(UserProjectPermissions.router)
app.include_router(Users.router)

# Crear tablas en la base de datos si no existen
def init_db():
    SQLModel.metadata.create_all(engine)
    fill_base_data()


init_db()
