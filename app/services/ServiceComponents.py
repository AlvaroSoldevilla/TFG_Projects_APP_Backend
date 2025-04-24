from sqlmodel import Session

import app.repositories.RepositoryComponents as rc
from app.schemas.Component import ComponentCreate, ComponentUpdate


async def get_all_components(session: Session):
    return await rc.get_all_components(session)


async def get_component_by_id(component_id: int, session: Session):
    return await rc.get_component_by_id(component_id, session)


async def create_component(component_data: ComponentCreate, session: Session):
    return await rc.create_component(component_data, session)


async def update_component(component_id: int, component_update: ComponentUpdate, session: Session):
    return await rc.update_component(component_id, component_update, session)


async def delete_component(component_id: int, session: Session):
    return await rc.delete_component(component_id, session)


async def get_components_by_board(board_id: int, session: Session):
    components = await rc.get_all_components(session)
    return [component for component in components if component.board_id == board_id]
