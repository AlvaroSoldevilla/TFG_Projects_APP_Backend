import app.repositories.RepositoryComponents as rc
from app.schemas.Component import ComponentCreate, ComponentUpdate


async def get_all_components():
    return rc.get_all_components()


async def get_component_by_id(component_id: int):
    return rc.get_component_by_id(component_id)


async def create_component(component_data: ComponentCreate):
    return rc.create_component(component_data)


async def update_component(component_id: int, component_update: ComponentUpdate):
    return rc.update_component(component_id, component_update)


async def delete_component(component_id: int):
    return rc.delete_component(component_id)


async def get_components_by_board(board_id: int):
    components = await rc.get_all_components()
    return [component for component in components if component.board_id == board_id]
