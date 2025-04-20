from fastapi import APIRouter, HTTPException

from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate, ProjectUserRead
import app.services.ServiceProjectUsers as spu

router = APIRouter(prefix="/project_users", tags=["Project Users"])


# Generic endpoints
@router.get("/", response_model=list[ProjectUserRead], status_code=200)
async def get_all_project_users():
    return spu.get_all_project_users()


@router.get("/{id}", response_model=ProjectUserRead, status_code=200)
async def get_project_user_by_id(id: int):
    return spu.get_project_user_by_id(id)


@router.post("/", status_code=200)
async def create_project_user(project_user_data: ProjectUserCreate):
    if spu.create_project_user(project_user_data):
        return {"Message": "Project user created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create project user")


@router.patch("/{id}", status_code=200)
async def update_project_user(id: int, project_user_update: ProjectUserUpdate):
    if spu.update_project_user(id, project_user_update):
        return {"Message": "Project user updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update project user")


@router.delete("/{id}", status_code=200)
async def delete_project_user(id: int):
    if spu.delete_project_user(id):
        return {"Message": "Project user deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete project user")


# Model Specific endpoints
@router.get("/user/{id}", response_model=list[ProjectUserRead], status_code=200)
async def get_project_users_by_user(id_user: int):
    return spu.get_project_user_by_user(id_user)


@router.get("/project/{id}", response_model=list[ProjectUserRead], status_code=200)
async def get_project_users_by_project(id_project: int):
    return spu.get_project_user_by_project(id_project)
