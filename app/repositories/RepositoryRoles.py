from sqlalchemy import select
from sqlmodel import Session

from app.models.Roles import Roles
from app.schemas.Role import RoleCreate, RoleUpdate


def get_all_roles(session: Session):
    query = select(Roles)
    roles = session.exec(query).scalars().all()

    return [Roles.model_validate(r) for r in roles]


def get_role_by_id(role_id: int, session: Session):
    return session.get(Roles, role_id)


def create_role(role_data: RoleCreate, session: Session):
    role = Roles(**role_data.model_dump())
    session.add(role)
    session.commit()
    session.refresh(role)

    return role


def update_role(role_id: int, role_update: RoleUpdate, session: Session):
    role = session.get(Roles, role_id)

    if not role:
        return False

    for k, v in role_update.model_dump(exclude_unset=True).items():
        setattr(role, k, v)

    session.add(role)
    session.commit()
    session.refresh(role)

    return True


def delete_role(role_id: int, session: Session):
    role = session.get(Roles, role_id)

    if not role:
        return False

    session.delete(role)
    session.commit()

    return True

