import app.repositories.RepositoryUsers as ru
from app.services.ServiceProjectUsers import get_project_user_by_project
from app.schemas.User import UserCreate, UserUpdate


async def get_all_users():
    return ru.get_all_users()


async def get_user_by_id(user_id: int):
    return ru.get_user_by_id(user_id)


async def create_user(user_data: UserCreate):
    return ru.create_user(user_data)


async def update_user(user_id: int, user_update: UserUpdate):
    return ru.update_user(user_id, user_update)


async def delete_user(user_id: int):
    return ru.delete_user(user_id)


async def get_users_by_project(id_project: int):
    all_users = ru.get_all_users()
    project_users = get_project_user_by_project(id_project)

    users = []
    for user in all_users:
        for project_user in project_users:
            if user.id == project_user.id_user:
                users.append(user)

    return users


async def authenticate_user(id_user: int, password: str):
    user = ru.get_user_by_id(id_user)

    if user.password == password:
        return True
    else:
        return False
