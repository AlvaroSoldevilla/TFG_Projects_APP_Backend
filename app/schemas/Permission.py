from sqlmodel import SQLModel


class PermissionCreate(SQLModel):
    name:   str


class PermissionRead(PermissionCreate):
    id:     int


class PermissionUpdate(SQLModel):
    name:   str | None = None
