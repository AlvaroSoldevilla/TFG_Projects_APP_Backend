from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.Project import ProjectCreate, ProjectUpdate, ProjectRead
import app.services.ServiceProjects as sp

router = APIRouter(prefix="/projects", tags=["Projects"])


# Generic endpoints
@router.get("/", dependencies=[Depends(JWTBearer())], response_model=list[ProjectRead], status_code=200)
def get_all_projects(session: Session = Depends(get_session)):
    return sp.get_all_projects(session)


@router.get("/{id}", dependencies=[Depends(JWTBearer())], response_model=ProjectRead, status_code=200)
def get_project_by_id(id: int, session: Session = Depends(get_session)):
    return sp.get_project_by_id(id, session)


@router.post("/", dependencies=[Depends(JWTBearer())], status_code=200, response_model=ProjectRead)
def create_project(project_data: ProjectCreate, session: Session = Depends(get_session)):
    project = sp.create_project(project_data, session)
    if project:
        return project
    else:
        raise HTTPException(status_code=400, detail="Could not create project")


@router.patch("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def update_project(id: int, project_update: ProjectUpdate, session: Session = Depends(get_session)):
    if sp.update_project(id, project_update, session):
        return {"Message": "Project updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update project")


@router.delete("/{id}", dependencies=[Depends(JWTBearer())], status_code=200)
def delete_project(id: int, session: Session = Depends(get_session)):
    if sp.delete_project(id, session):
        return {"Message": "Project deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete project")


# Model Specific endpoints
@router.get("/user/{id}", dependencies=[Depends(JWTBearer())], response_model=list[ProjectRead], status_code=200)
def get_projects_by_user(id: int, session: Session = Depends(get_session)):
    return sp.get_projects_by_user(id, session)
