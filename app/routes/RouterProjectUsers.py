from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.ProjectUser import ProjectUserCreate, ProjectUserUpdate, ProjectUserRead
import app.services.ServiceProjectUsers as spu

router = APIRouter(prefix="/project_users", tags=["Project Users"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[ProjectUserRead], status_code=200)
def get_all_project_users(session: Session = Depends(get_session)):
    return spu.get_all_project_users(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=ProjectUserRead, status_code=200)
def get_project_user_by_id(id: int, session: Session = Depends(get_session)):
    project_user = spu.get_project_user_by_id(id, session)
    if project_user is None:
        raise HTTPException(status_code=404, detail="ProjectUser not found")
    else:
        return project_user


@router.post("", dependencies=[Depends(jwt_scheme)], status_code=200, response_model=ProjectUserRead)
def create_project_user(project_user_data: ProjectUserCreate, session: Session = Depends(get_session)):
    project_user = spu.create_project_user(project_user_data, session)
    if project_user:
        return project_user
    else:
        raise HTTPException(status_code=400, detail="Could not create project user")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_project_user(id: int, project_user_update: ProjectUserUpdate, session: Session = Depends(get_session)):
    if spu.update_project_user(id, project_user_update, session):
        return {"Message": "Project user updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update project user")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_project_user(id: int, session: Session = Depends(get_session)):
    if spu.delete_project_user(id, session):
        return {"Message": "Project user deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete project user")


# Model Specific endpoints
@router.get("/user/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[ProjectUserRead], status_code=200)
def get_project_users_by_user(id: int, session: Session = Depends(get_session)):
    return spu.get_project_user_by_user(id, session)


@router.get("/project/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[ProjectUserRead], status_code=200)
def get_project_users_by_project(id: int, session: Session = Depends(get_session)):
    return spu.get_project_user_by_project(id, session)

@router.get("/project/{id_project}/user/{id_user}", dependencies=[Depends(jwt_scheme)], response_model=ProjectUserRead, status_code=200)
def get_project_user_by_project_and_user(id_project: int, id_user: int, session: Session = Depends(get_session)):
    return spu.get_project_user_by_project_and_user(id_project, id_user, session)
