from sqlmodel import Session

import app.repositories.RepositoryProjects as rp
from app.services.ServiceProjectUsers import get_project_user_by_user
from app.schemas.Project import ProjectCreate, ProjectUpdate


async def get_all_projects(session: Session):
    return await rp.get_all_projects(session)


async def get_project_by_id(project_id: int, session: Session):
    return await rp.get_project_by_id(project_id, session)


async def create_project(project_data: ProjectCreate, session: Session):
    return await rp.create_project(project_data, session)


async def update_project(project_id: int, project_update: ProjectUpdate, session: Session):
    return await rp.update_project(project_id, project_update, session)


async def delete_project(project_id: int, session: Session):
    return await rp.delete_project(project_id, session)


async def get_projects_by_user(id_user: int, session: Session):
    all_projects = await rp.get_all_projects(session)
    user_projects = await get_project_user_by_user(id_user, session)

    project = []
    for project in all_projects:
        for user_project in user_projects:
            if project.id == user_project.id_project:
                project.append(project)

    return project
