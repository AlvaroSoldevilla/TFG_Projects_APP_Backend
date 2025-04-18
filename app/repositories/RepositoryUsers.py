from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Users import Users
from app.schemas.User import UserCreate, UserUpdate


async def get_all_users(session: Session = Depends(get_session())):
    query = select(Users)
    users = session.exec(query).scalar().all()

    return [Users.model_validate(u) for u in users]


async def get_user_by_id(user_id: int, session: Session = Depends(get_session())):
    return session.get(Users, user_id)


async def create_user(user_data: UserCreate, session: Session = Depends(get_session())):
    user = Users(**user_data.model_dump())
    session.add(user)
    session.commit()
    session.refresh(user)

    return True


async def update_user(user_id: int, user_update: UserUpdate, session: Session = Depends(get_session())):
    user = session.get(Users, user_id)

    if not user:
        return False

    for k, v in user_update.model_dump(exclude_unset=True).items():
        setattr(user, k, v)

    session.add(user)
    session.commit()
    session.refresh(user)

    return True


async def delete_user(user_id: int, session: Session = Depends(get_session())):
    user = session.get(Users, user_id)

    if not user:
        return False

    session.delete(user)
    session.commit()

    return True
