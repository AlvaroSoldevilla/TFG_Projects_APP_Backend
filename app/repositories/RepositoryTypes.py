from sqlalchemy import select
from sqlmodel import Session

from app.models.Types import Types
from app.schemas.Type import TypeCreate, TypeUpdate


def get_all_types(session: Session):
    query = select(Types)
    component_types = session.exec(query).scalars().all()

    return [Types.model_validate(t) for t in component_types]


def get_type_by_id(type_id: int, session: Session):
    return session.get(Types, type_id)


def create_type(type_data: TypeCreate, session: Session):
    component_type = Types(**type_data.model_dump())
    session.add(component_type)
    session.commit()
    session.refresh(component_type)

    return True


def update_type(type_id: int, type_update: TypeUpdate, session: Session):
    component_type = session.get(Types, type_id)

    if not component_type:
        return False

    for k, v in type_update.model_dump(exclude_unset=True).items():
        setattr(component_type, k, v)

    session.add(component_type)
    session.commit()
    session.refresh(component_type)

    return True


def delete_type(type_id: int, session: Session):
    component_type = session.get(Types, type_id)

    if not component_type:
        return False

    session.delete(component_type)
    session.commit()

    return True
