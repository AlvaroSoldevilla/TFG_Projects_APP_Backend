import app.repositories.RepositoryProjectUsers as rpu
from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate


async def get_all_project_users():
    return rpu.get_all_project_users()


async def get_project_user_by_id(project_user_id: int):
    return rpu.get_project_user_by_id(project_user_id)


async def create_project_user(project_user_data: ProjectUserCreate):
    return rpu.create_project_user(project_user_data)


async def update_project_user(project_user_id: int, project_user_update: ProjectUserUpdate):
    return rpu.update_project_user(project_user_id, project_user_update)


async def delete_project_user(project_user_id: int):
    return rpu.delete_project_user(project_user_id)


async def get_project_user_by_user(id_user: int):
    project_users = rpu.get_all_project_users()
    return [project_user for project_user in project_users if project_user.id_user == id_user]


async def get_project_user_by_project(id_project: int):
    project_users = rpu.get_all_project_users()
    return [project_user for project_user in project_users if project_user.id_project == id_project]
