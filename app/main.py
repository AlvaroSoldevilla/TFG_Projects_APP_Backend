from fastapi import FastAPI
from app.routes import (RouterComponents, RouterConceptBoards, RouterConcepts, RouterPermissions, RouterPriorities,
                        RouterProjects, RouterProjectUsers, RouterRoles, RouterTaskBoards, RouterTaskDependencies,
                        RouterTaskProgress, RouterTasks, RouterTaskSections, RouterTypes, RouterUserProjectPermissions,
                        RouterUsers)
from app.db.session import engine, get_session
from sqlmodel import SQLModel

from app.repositories.RepositoryPriorities import create_priority
from app.schemas.Priority import PriorityCreate
from app.models.Priorities import Priorities

from app.repositories.RepositoryTypes import create_type
from app.schemas.Type import TypeCreate
from app.models.Types import Types

from app.repositories.RepositoryPermissions import create_permission
from app.schemas.Permission import PermissionCreate
from app.models.Permissions import Permissions

app = FastAPI()

# Registrar las rutas
app.include_router(RouterComponents.router)
app.include_router(RouterConceptBoards.router)
app.include_router(RouterConcepts.router)
app.include_router(RouterPermissions.router)
app.include_router(RouterPriorities.router)
app.include_router(RouterProjects.router)
app.include_router(RouterProjectUsers.router)
app.include_router(RouterRoles.router)
app.include_router(RouterTaskBoards.router)
app.include_router(RouterTaskDependencies.router)
app.include_router(RouterTaskProgress.router)
app.include_router(RouterTasks.router)
app.include_router(RouterTaskSections.router)
app.include_router(RouterTypes.router)
app.include_router(RouterUserProjectPermissions.router)
app.include_router(RouterUsers.router)


# Crear tablas en la base de datos si no existen
async def init_db():
    SQLModel.metadata.create_all(engine)
    await create_permissions()
    await create_component_types()
    await create_priorities()


async def create_permissions():
    with next(get_session()) as session:
        if session.get(Permissions, 1) is None:
            await create_permission(PermissionCreate(name="full_permissions"), session)

            await create_permission(PermissionCreate(name="read_tasks"), session)
            await create_permission(PermissionCreate(name="create_tasks"), session)
            await create_permission(PermissionCreate(name="create_task_boards"), session)
            await create_permission(PermissionCreate(name="create_task_sections"), session)
            await create_permission(PermissionCreate(name="edit_tasks"), session)
            await create_permission(PermissionCreate(name="edit_task_boards"), session)
            await create_permission(PermissionCreate(name="edit_sections"), session)
            await create_permission(PermissionCreate(name="delete_tasks"), session)
            await create_permission(PermissionCreate(name="delete_task_boards"), session)
            await create_permission(PermissionCreate(name="delete_task_sections"), session)

            await create_permission(PermissionCreate(name="full_task_permissions"), session)

            await create_permission(PermissionCreate(name="read_concepts"), session)
            await create_permission(PermissionCreate(name="create_concepts"), session)
            await create_permission(PermissionCreate(name="edit_concepts"), session)
            await create_permission(PermissionCreate(name="delete_concepts"), session)

            await create_permission(PermissionCreate(name="full_concept_permissions"), session)


async def create_component_types():
    with next(get_session()) as session:
        if session.get(Types, 1) is None:
            await create_type(TypeCreate(name="ConceptBoard"), session)
            await create_type(TypeCreate(name="Note"), session)
            await create_type(TypeCreate(name="Container"), session)
            await create_type(TypeCreate(name="Table"), session)
            await create_type(TypeCreate(name="Line"), session)


async def create_priorities():
    with next(get_session()) as session:
        if session.get(Priorities, 1) is None:
            await create_priority(PriorityCreate(name="Maximum priority"), session)
            await create_priority(PriorityCreate(name="Medium priority"), session)
            await create_priority(PriorityCreate(name="Minimum priority"), session)


@app.on_event("startup")
async def on_startup():
    await init_db()
