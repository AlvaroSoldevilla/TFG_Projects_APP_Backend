from sqlmodel import Session

import app.repositories.RepositoryUsers as ru
from app.services.ServiceProjectUsers import get_project_user_by_project
from app.schemas.User import UserCreate, UserUpdate, UserAuthenticate, UserEmail


def get_all_users(session: Session):
    return ru.get_all_users(session)


def get_user_by_id(user_id: int, session: Session):
    return ru.get_user_by_id(user_id, session)


def create_user(user_data: UserCreate, session: Session):
    return ru.create_user(user_data, session)


def update_user(user_id: int, user_update: UserUpdate, session: Session):
    existing_user = ru.get_user_by_id(user_id, session)
    if user_update.password is None:
        user_update.password = existing_user.password

    if user_update.email is not None and existing_user.email != user_update.email:
        if get_user_by_email(UserEmail(email=user_update.email), session) is None:
            return ru.update_user(user_id, user_update, session)
        else:
            return None

    return ru.update_user(user_id, user_update, session)


def delete_user(user_id: int, session: Session):
    return ru.delete_user(user_id, session)


def get_users_by_project(id_project: int, session: Session):
    all_users = ru.get_all_users(session)
    project_users = get_project_user_by_project(id_project, session)

    users = []
    for user in all_users:
        for project_user in project_users:
            if user.id == project_user.id_user:
                users.append(user)

    return users


def authenticate_user(user_data: UserAuthenticate, session: Session):
    user = ru.get_user_by_mail(user_data.email, session)

    if user is not None:
        if user[0].password == user_data.password:
            return user[0]
        else:
            return None
    else:
        return None


def get_user_by_email(user_email: UserEmail, session: Session):
    return ru.get_user_by_mail(user_email.email, session)
