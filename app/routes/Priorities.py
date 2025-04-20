from fastapi import APIRouter, HTTPException

from app.schemas.Priority import PriorityCreate, PriorityUpdate, PriorityRead
import app.services.ServicePriorities as sp

router = APIRouter(prefix="/priorities", tags=["Priorities"])


# Generic endpoints
@router.get("/", response_model=list[PriorityRead], status_code=200)
async def get_all_priorities():
    return sp.get_all_priorities()


@router.get("/{id}", response_model=PriorityRead, status_code=200)
async def get_priority_by_id(id: int):
    return sp.get_priority_by_id(id)


@router.post("/", status_code=200)
async def create_priority(priority_data: PriorityCreate):
    if sp.create_priority(priority_data):
        return {"Message": "Priority created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create priority")


@router.patch("/{id}", status_code=200)
async def update_priority(id: int, priority_update: PriorityUpdate):
    if sp.update_priority(id, priority_update):
        return {"Message": "Priority updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update priority")


@router.delete("/{id}", status_code=200)
async def delete_priority(id: int):
    if sp.delete_priority(id):
        return {"Message": "Priority deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete priority")
