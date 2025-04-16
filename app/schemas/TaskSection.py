from sqlmodel import SQLModel


class TaskSectionCreate(SQLModel):
    id_board:   int
    title:      str


class TaskSectionRead(TaskSectionCreate):
    id:         int


class TaskSectionUpdate(SQLModel):
    id_board:   int | None = None
    title:      str | None = None
