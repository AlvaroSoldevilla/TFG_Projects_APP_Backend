from sqlmodel import SQLModel


class PriorityCreate(SQLModel):
    name:               str
    color:              str
    priority_value:     int


class PriorityRead(PriorityCreate):
    id:                 int


class PriorityUpdate(SQLModel):
    name:               str | None = None
    color:              str | None = None
    priority_value:     int | None = None
