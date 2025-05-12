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
def init_db():
    SQLModel.metadata.create_all(engine)
    create_permissions()
    create_component_types()
    create_priorities()


def create_permissions():
    with next(get_session()) as session:
        if session.get(Permissions, 1) is None:
            create_permission(PermissionCreate(name="full_permissions"), session)

            create_permission(PermissionCreate(name="read_tasks"), session)
            create_permission(PermissionCreate(name="create_tasks"), session)
            create_permission(PermissionCreate(name="create_task_boards"), session)
            create_permission(PermissionCreate(name="create_task_sections"), session)
            create_permission(PermissionCreate(name="edit_tasks"), session)
            create_permission(PermissionCreate(name="edit_task_boards"), session)
            create_permission(PermissionCreate(name="edit_sections"), session)
            create_permission(PermissionCreate(name="delete_tasks"), session)
            create_permission(PermissionCreate(name="delete_task_boards"), session)
            create_permission(PermissionCreate(name="delete_task_sections"), session)

            create_permission(PermissionCreate(name="full_task_permissions"), session)

            create_permission(PermissionCreate(name="read_concepts"), session)
            create_permission(PermissionCreate(name="create_concepts"), session)
            create_permission(PermissionCreate(name="edit_concepts"), session)
            create_permission(PermissionCreate(name="delete_concepts"), session)

            create_permission(PermissionCreate(name="full_concept_permissions"), session)


def create_component_types():
    with next(get_session()) as session:
        if session.get(Types, 1) is None:
            create_type(TypeCreate(name="ConceptBoard"), session)
            create_type(TypeCreate(name="Note"), session)
            create_type(TypeCreate(name="Container"), session)
            create_type(TypeCreate(name="Table"), session)
            create_type(TypeCreate(name="Line"), session)


def create_priorities():
    with next(get_session()) as session:
        if session.get(Priorities, 1) is None:
            create_priority(PriorityCreate(name="Maximum priority", color="#e83023", priority_value=1), session)
            create_priority(PriorityCreate(name="Medium priority", color="#e8db23", priority_value=2), session)
            create_priority(PriorityCreate(name="Minimum priority", color="#23e841", priority_value=3), session)


init_db()
