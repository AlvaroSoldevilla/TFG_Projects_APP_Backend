from sqlmodel import Session

import app.repositories.RepositoryProjects as rp
from app.services.ServiceProjectUsers import get_project_user_by_user
from app.schemas.Project import ProjectCreate, ProjectUpdate


def get_all_projects(session: Session):
    return rp.get_all_projects(session)


def get_project_by_id(project_id: int, session: Session):
    return rp.get_project_by_id(project_id, session)


def create_project(project_data: ProjectCreate, session: Session):
    return rp.create_project(project_data, session)


def update_project(project_id: int, project_update: ProjectUpdate, session: Session):
    return rp.update_project(project_id, project_update, session)


def delete_project(project_id: int, session: Session):
    return rp.delete_project(project_id, session)


def get_projects_by_user(id_user: int, session: Session):
    all_projects = rp.get_all_projects(session)
    user_projects = get_project_user_by_user(id_user, session)

    projects = []
    for project in all_projects:
        for user_project in user_projects:
            if project.id == user_project.id_project:
                projects.append(project)

    return projects
