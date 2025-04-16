from sqlmodel import SQLModel


class PriorityCreate(SQLModel):
    name:   str


class PriorityRead(PriorityCreate):
    id:     int


class PriorityUpdate(SQLModel):
    name:   str | None = None
