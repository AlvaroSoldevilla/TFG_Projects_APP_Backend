from sqlmodel import Session

import app.repositories.RepositoryUsers as ru
from app.services.ServiceProjectUsers import get_project_user_by_project
from app.schemas.User import UserCreate, UserUpdate, UserAuthenticate


async def get_all_users(session: Session):
    return await ru.get_all_users(session)


async def get_user_by_id(user_id: int, session: Session):
    return await ru.get_user_by_id(user_id, session)


async def create_user(user_data: UserCreate, session: Session):
    return await ru.create_user(user_data, session)


async def update_user(user_id: int, user_update: UserUpdate, session: Session):
    return await ru.update_user(user_id, user_update, session)


async def delete_user(user_id: int, session: Session):
    return await ru.delete_user(user_id, session)


async def get_users_by_project(id_project: int, session: Session):
    all_users = await ru.get_all_users(session)
    project_users = await get_project_user_by_project(id_project, session)

    users = []
    for user in all_users:
        for project_user in project_users:
            if user.id == project_user.id_user:
                users.append(user)

    return users


async def authenticate_user(user_data: UserAuthenticate, session: Session):
    user = await ru.get_user_by_mail(user_data.email, session)

    if user is not None:
        if user.password == user_data.password:
            return True
        else:
            return False
    else:
        return False
