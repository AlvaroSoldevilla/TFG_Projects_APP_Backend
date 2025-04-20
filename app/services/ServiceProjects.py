import app.repositories.RepositoryProjects as rp
from app.services.ServiceProjectUsers import get_project_user_by_user
from app.schemas.Project import ProjectCreate, ProjectUpdate


async def get_all_projects():
    return rp.get_all_projects()


async def get_project_by_id(project_id: int):
    return rp.get_project_by_id(project_id)


async def create_project(project_data: ProjectCreate):
    return rp.create_project(project_data)


async def update_project(project_id: int, project_update: ProjectUpdate):
    return rp.update_project(project_id, project_update)


async def delete_project(project_id: int):
    return rp.delete_project(project_id)


async def get_projects_by_user(id_user: int):
    all_projects = rp.get_all_projects()
    user_projects = get_project_user_by_user(id_user)

    project = []
    for project in all_projects:
        for user_project in user_projects:
            if project.id == user_project.id_project:
                project.append(project)

    return project