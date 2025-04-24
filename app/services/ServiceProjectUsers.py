from sqlmodel import Session

import app.repositories.RepositoryProjectUsers as rpu
from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate


async def get_all_project_users(session: Session):
    return await rpu.get_all_project_users(session)


async def get_project_user_by_id(project_user_id: int, session: Session):
    return await rpu.get_project_user_by_id(project_user_id, session)


async def create_project_user(project_user_data: ProjectUserCreate, session: Session):
    return await rpu.create_project_user(project_user_data, session)


async def update_project_user(project_user_id: int, project_user_update: ProjectUserUpdate, session: Session):
    return await rpu.update_project_user(project_user_id, project_user_update, session)


async def delete_project_user(project_user_id: int, session: Session):
    return await rpu.delete_project_user(project_user_id, session)


async def get_project_user_by_user(id_user: int, session: Session):
    project_users = await rpu.get_all_project_users(session)
    return [project_user for project_user in project_users if project_user.id_user == id_user]


async def get_project_user_by_project(id_project: int, session: Session):
    project_users = await rpu.get_all_project_users(session)
    return [project_user for project_user in project_users if project_user.id_project == id_project]
