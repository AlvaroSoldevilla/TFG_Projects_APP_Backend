from sqlmodel import Session

import app.repositories.RepositoryProjectUsers as rpu
from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate


def get_all_project_users(session: Session):
    return rpu.get_all_project_users(session)


def get_project_user_by_id(project_user_id: int, session: Session):
    return rpu.get_project_user_by_id(project_user_id, session)


def create_project_user(project_user_data: ProjectUserCreate, session: Session):
    return rpu.create_project_user(project_user_data, session)


def update_project_user(project_user_id: int, project_user_update: ProjectUserUpdate, session: Session):
    return rpu.update_project_user(project_user_id, project_user_update, session)


def delete_project_user(project_user_id: int, session: Session):
    return rpu.delete_project_user(project_user_id, session)


def get_project_user_by_user(id_user: int, session: Session):
    project_users = rpu.get_all_project_users(session)
    return [project_user for project_user in project_users if project_user.id_user == id_user]


def get_project_user_by_project(id_project: int, session: Session):
    project_users = rpu.get_all_project_users(session)
    return [project_user for project_user in project_users if project_user.id_project == id_project]
