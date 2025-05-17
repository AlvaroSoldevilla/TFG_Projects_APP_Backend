from sqlalchemy import select
from sqlmodel import Session

from app.models.Users import Users
from app.schemas.User import UserCreate, UserUpdate


def get_all_users(session: Session):
    query = select(Users)
    users = session.exec(query).scalars().all()

    return [Users.model_validate(u) for u in users]


def get_user_by_id(user_id: int, session: Session):
    return session.get(Users, user_id)


def create_user(user_data: UserCreate, session: Session):
    if not mail_exists(user_data.email, session):
        user = Users(**user_data.model_dump())
        session.add(user)
        session.commit()
        session.refresh(user)

        return user
    return None


def update_user(user_id: int, user_update: UserUpdate, session: Session):
    user = session.get(Users, user_id)

    if not user:
        return False

    for k, v in user_update.model_dump(exclude_unset=True).items():
        if k == "email" and not mail_exists(v, session):
            setattr(user, k, v)

    session.add(user)
    session.commit()
    session.refresh(user)

    return True


def delete_user(user_id: int, session: Session):
    user = session.get(Users, user_id)

    if not user:
        return False

    session.delete(user)
    session.commit()

    return True


def mail_exists(email: str, session: Session):
    query = select(Users).where(Users.email == email)
    user = session.exec(query).first()

    if user is None:
        return False
    else:
        return True


def get_user_by_mail(email: str, session: Session):
    query = select(Users).where(Users.email == email)
    user = session.exec(query).first()

    return user if user is not None else None
