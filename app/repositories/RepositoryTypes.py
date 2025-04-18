from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Types import Types
from app.schemas.Type import TypeCreate, TypeUpdate


async def get_all_types(session: Session = Depends(get_session())):
    query = select(Types)
    component_types = session.exec(query).scalar().all()

    return [Types.model_validate(t) for t in component_types]


async def get_type_by_id(type_id: int, session: Session = Depends(get_session())):
    return session.get(Types, type_id)


async def create_type(type_data: TypeCreate, session: Session = Depends(get_session())):
    component_type = Types(**type_data.model_dump())
    session.add(component_type)
    session.commit()
    session.refresh(component_type)

    return True


async def update_type(type_id: int, type_update: TypeUpdate, session: Session = Depends(get_session())):
    component_type = session.get(Types, type_id)

    if not component_type:
        return False

    for k, v in type_update.model_dump(exclude_unset=True).items():
        setattr(component_type, k, v)

    session.add(component_type)
    session.commit()
    session.refresh(component_type)

    return True


async def delete_type(type_id: int, session: Session = Depends(get_session())):
    component_type = session.get(Types, type_id)

    if not component_type:
        return False

    session.delete(component_type)
    session.commit()

    return True
