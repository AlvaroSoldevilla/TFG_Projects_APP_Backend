from sqlalchemy import select
from sqlmodel import Session

from app.models.Components import Components
from app.schemas.Component import ComponentCreate, ComponentUpdate


class ComponentsRead:
    pass


def get_all_components(session: Session):
    query = select(Components)
    components = session.exec(query).scalars().all()

    return [Components.model_validate(c) for c in components]


def get_component_by_id(component_id: int, session: Session):
    return session.get(Components, component_id)


def create_component(component_data: ComponentCreate, session: Session):
    component = Components(**component_data.model_dump())
    session.add(component)
    session.commit()
    session.refresh(component)

    return True


def update_component(component_id: int, component_update: ComponentUpdate, session: Session):
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


def delete_component(component_id: int, session: Session):
    component = session.get(Components, component_id)

    if not component:
        return False

    session.delete(component)
    session.commit()

    return True
