from fastapi import APIRouter, HTTPException

from app.schemas.Project import ProjectCreate, ProjectUpdate, ProjectRead
import app.services.ServiceProjects as sp

router = APIRouter(prefix="/projects", tags=["Projects"])


# Generic endpoints
@router.get("/", response_model=list[ProjectRead], status_code=200)
async def get_all_projects():
    return sp.get_all_projects()


@router.get("/{id}", response_model=ProjectRead, status_code=200)
async def get_project_by_id(id: int):
    return sp.get_project_by_id(id)


@router.post("/", status_code=200)
async def create_project(project_data: ProjectCreate):
    if sp.create_project(project_data):
        return {"Message": "Project created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create project")


@router.patch("/{id}", status_code=200)
async def update_project(id: int, project_update: ProjectUpdate):
    if sp.update_project(id, project_update):
        return {"Message": "Project updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update project")


@router.delete("/{id}", status_code=200)
async def delete_project(id: int):
    if sp.delete_project(id):
        return {"Message": "Project deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete project")


# Model Specific endpoints
@router.get("/user/{id}", response_model=list[ProjectRead], status_code=200)
async def get_projects_by_user(id_user: int):
    return sp.get_projects_by_user(id_user)
