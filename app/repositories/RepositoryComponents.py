from fastapi import Depends
from sqlalchemy import select
from sqlmodel import Session
from app.db.session import get_session
from app.models.Components import Components
from app.schemas.Component import ComponentCreate, ComponentUpdate


async def get_all_components(session: Session = Depends(get_session())):
    query = select(Components)
    components = session.exec(query).scalar().all()

    return [Components.model_validate(c) for c in components]


async def get_component_by_id(component_id: int, session: Session = Depends(get_session())):
    return session.get(Components, component_id)


async def create_component(component_data: ComponentCreate, session: Session = Depends(get_session())):
    component = Components(**component_data.model_dump())
    session.add(component)
    session.commit()
    session.refresh(component)

    return True


async def update_component(component_id: int, component_update: ComponentUpdate, session: Session = Depends(get_session())):
    component = session.get(Components, component_id)

    if not component:
        return False

    component_dict = component_update.model_dump(exclude_unset=True)

    for k, v in component_dict.items():
        setattr(component, k, v)

    session.add(component)
    session.commit()
    session.refresh(component)

    return True


async def delete_component(component_id: int, session: Session = Depends(get_session())):
    component = session.get(Components, component_id)

    if not component:
        return False

    session.delete(component)
    session.commit()

    return True
