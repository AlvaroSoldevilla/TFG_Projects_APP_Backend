from fastapi import APIRouter, HTTPException, Depends
from sqlmodel import Session
import app.auth.auth_handler as auth
from app.auth.auth_bearer import JWTBearer

from app.db.session import get_session
from app.schemas.User import UserCreate, UserUpdate, UserRead, UserAuthenticate, UserEmail, RefreshToken
import app.services.ServiceUsers as su

router = APIRouter(prefix="/users", tags=["Users"])
jwt_scheme = JWTBearer()


# Generic endpoints
@router.get("", dependencies=[Depends(jwt_scheme)], response_model=list[UserRead], status_code=200)
def get_all_users(session: Session = Depends(get_session)):
    return su.get_all_users(session)


@router.get("/{id}", dependencies=[Depends(jwt_scheme)], response_model=UserRead, status_code=200)
def get_user_by_id(id: int, session: Session = Depends(get_session)):
    user = su.get_user_by_id(id, session)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    else:
        return user


@router.post("", status_code=200, response_model=UserRead)
def create_user(user_data: UserCreate, session: Session = Depends(get_session)):
    user = su.create_user(user_data, session)
    if user:
        return user
    else:
        raise HTTPException(status_code=400, detail="Could not create user")


@router.patch("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def update_user(id: int, user_update: UserUpdate, session: Session = Depends(get_session)):
    if su.update_user(id, user_update, session):
        return {"Message": "User updated"}
    else:
        raise HTTPException(status_code=400, detail="Could not update user")


@router.delete("/{id}", dependencies=[Depends(jwt_scheme)], status_code=200)
def delete_user(id: int, session: Session = Depends(get_session)):
    if su.delete_user(id, session):
        return {"Message": "User deleted"}
    else:
        raise HTTPException(status_code=400, detail="Could not delete user")


# Model Specific endpoints
@router.get("/project/{id}", dependencies=[Depends(jwt_scheme)], response_model=list[UserRead], status_code=200)
def get_users_by_project(id: int, session: Session = Depends(get_session)):
    return su.get_users_by_project(id, session)


@router.post("/email", dependencies=[Depends(jwt_scheme)], response_model=UserRead, status_code=200)
def get_user_by_email(user_email: UserEmail, session: Session = Depends(get_session)):
    user = su.get_user_by_email(user_email, session)
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=400, detail="Could not find user")


@router.post("/auth", response_model=UserRead, status_code=200)
def authenticate_user(user_data: UserAuthenticate, session: Session = Depends(get_session)):
    user = su.authenticate_user(user_data, session)
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=400, detail="Could not authenticate user")


@router.post("/token", status_code=200)
def get_token(user_data: UserAuthenticate, session: Session = Depends(get_session)):
    user = su.authenticate_user(user_data, session)
    if user is not None:
        return auth.sign_jwt(user_data.email)
    else:
        raise HTTPException(status_code=400, detail="Could not generate token")


@router.post("/refresh", status_code=200)
def refresh_token(user_email_token: RefreshToken, session: Session = Depends(get_session)):
    user = su.get_user_by_email(UserEmail(email=user_email_token.email), session)
    if user is not None:
        return auth.refresh_jwt(user_email_token.token, user_email_token.email)
    else:
        raise HTTPException(status_code=400, detail="Incorrect credentials")
