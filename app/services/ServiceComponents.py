import app.repositories.RepositoryComponents as rc
from app.schemas.Component import ComponentCreate, ComponentUpdate


async def get_all_components():
    return await rc.get_all_components()


async def get_component_by_id(component_id: int):
    return await rc.get_component_by_id(component_id)


async def create_component(component_data: ComponentCreate):
    return await rc.create_component(component_data)


async def update_component(component_id: int, component_update: ComponentUpdate):
    return await rc.update_component(component_id, component_update)


async def delete_component(component_id: int):
    return await rc.delete_component(component_id)


async def get_components_by_board(board_id: int):
    components = await rc.get_all_components()
    return [component for component in components if component.board_id == board_id]
