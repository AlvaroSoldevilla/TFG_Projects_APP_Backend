from sqlmodel import Session

import app.repositories.RepositoryComponents as rc
from app.schemas.Component import ComponentCreate, ComponentUpdate


def get_all_components(session: Session):
    return rc.get_all_components(session)


def get_component_by_id(component_id: int, session: Session):
    return rc.get_component_by_id(component_id, session)


def create_component(component_data: ComponentCreate, session: Session):
    return rc.create_component(component_data, session)


def update_component(component_id: int, component_update: ComponentUpdate, session: Session):
    return rc.update_component(component_id, component_update, session)


def delete_component(component_id: int, session: Session):
    return rc.delete_component(component_id, session)


def get_components_by_board(board_id: int, session: Session):
    components = rc.get_all_components(session)
    return [component for component in components if component.board_id == board_id]
