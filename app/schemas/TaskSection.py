from sqlmodel import SQLModel


class TaskSectionCreate(SQLModel):
    id_board:               int
    title:                  str
    id_default_progress:    int
    order:                  int | None = 0


class TaskSectionRead(TaskSectionCreate):
    id:                     int


class TaskSectionUpdate(SQLModel):
    id_board:               int | None = None
    id_default_progress:    int | None = None
    title:                  str | None = None
    order:                  int | None = None
