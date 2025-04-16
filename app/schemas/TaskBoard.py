from sqlmodel import SQLModel


class TaskBoardCreate(SQLModel):
    id_project:     int
    title:          str
    description:    str | None = ""


class TaskBoardRead(TaskBoardCreate):
    id:             int


class TaskBoardUpdate(SQLModel):
    id_project:     int | None = None
    title:          str | None = None
    description:    str | None = None
