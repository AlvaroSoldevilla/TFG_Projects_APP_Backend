from sqlmodel import SQLModel


class RoleCreate(SQLModel):
    name:           str
    description:    str | None = None


class RoleRead(RoleCreate):
    id:             int


class RoleUpdate(SQLModel):
    name:           str | None = None
    description:    str | None = None
