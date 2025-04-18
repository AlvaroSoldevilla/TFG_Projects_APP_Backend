from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Roles import Roles
from app.schemas.Role import RoleCreate, RoleUpdate


async def get_all_roles(session: Session = Depends(get_session())):
    query = select(Roles)
    roles = session.exec(query).scalar().all()

    return [Roles.model_validate(r) for r in roles]


async def get_role_by_id(role_id: int, session: Session = Depends(get_session())):
    return session.get(Roles, role_id)


async def create_role(role_data: RoleCreate, session: Session = Depends(get_session())):
    role = Roles(**role_data.model_dump())
    session.add(role)
    session.commit()
    session.refresh(role)

    return True


async def update_role(role_id: int, role_update: RoleUpdate, session: Session = Depends(get_session())):
    role = session.get(Roles, role_id)

    if not role:
        return False

    for k, v in role_update.model_dump(exclude_unset=True).items():
        setattr(role, k, v)

    session.add(role)
    session.commit()
    session.refresh(role)

    return True


async def delete_role(role_id: int, session: Session = Depends(get_session())):
    role = session.get(Roles, role_id)

    if not role:
        return False

    session.delete(role)
    session.commit()

    return True

