from sqlmodel import SQLModel


class TypeCreate(SQLModel):
    name:           str


class TypeRead(TypeCreate):
    id:         int


class TypeUpdate(SQLModel):
    name:           str | None = None
