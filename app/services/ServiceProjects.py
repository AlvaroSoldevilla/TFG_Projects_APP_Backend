import app.repositories.RepositoryProjects as rp
from app.services.ServiceProjectUsers import get_project_user_by_user
from app.schemas.Project import ProjectCreate, ProjectUpdate


async def get_all_projects():
    return await rp.get_all_projects()


async def get_project_by_id(project_id: int):
    return await rp.get_project_by_id(project_id)


async def create_project(project_data: ProjectCreate):
    return await rp.create_project(project_data)


async def update_project(project_id: int, project_update: ProjectUpdate):
    return await rp.update_project(project_id, project_update)


async def delete_project(project_id: int):
    return await rp.delete_project(project_id)


async def get_projects_by_user(id_user: int):
    all_projects = await rp.get_all_projects()
    user_projects = await get_project_user_by_user(id_user)

    project = []
    for project in all_projects:
        for user_project in user_projects:
            if project.id == user_project.id_project:
                project.append(project)

    return project
