from sqlmodel import SQLModel


class UserProjectPermissionCreate(SQLModel):
    id_permission:  int
    id_user:        int
    id_project:     int


class UserProjectPermissionRead(UserProjectPermissionCreate):
    id:             int


class UserProjectPermissionUpdate(SQLModel):
    id_permission:  int | None = None
    id_user:        int | None = None
    id_project:     int | None = None
