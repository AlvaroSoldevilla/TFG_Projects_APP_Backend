from fastapi import APIRouter, HTTPException

from app.schemas.User import UserCreate, UserUpdate, UserRead, UserAuthenticate
import app.services.ServiceUsers as su

router = APIRouter(prefix="/users", tags=["Users"])


# Generic endpoints
@router.get("/", response_model=list[UserRead], status_code=200)
async def get_all_users():
    return su.get_all_users()


@router.get("/{id}", response_model=UserRead, status_code=200)
async def get_user_by_id(id: int):
    return su.get_user_by_id(id)


@router.post("/", status_code=200)
async def create_user(user_data: UserCreate):
    if su.create_user(user_data):
        return {"Message": "User created"}
    else:
        raise HTTPException(status_code=400, detail="Could not create user")


@router.patch("/{id}", status_code=200)
async def update_user(id: int, user_update: UserUpdate):
    if su.update_user(id, user_update):
        return {"Message": "User updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update user")


@router.delete("/{id}", status_code=200)
async def delete_user(id: int):
    if su.delete_user(id):
        return {"Message": "User deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete user")


# Model Specific endpoints
@router.get("/project/{id}", response_model=list[UserRead], status_code=200)
async def get_users_by_project(id: int):
    return su.get_project_user_by_project(id)


@router.post("/auth/", status_code=200)
async def authenticate_user(user_data: UserAuthenticate):
    if su.authenticate_user(user_data):
        return {"Message": "User Authenticated"}
    else:
        raise HTTPException(status_code=400, detail="Could not authenticate user")
