from sqlmodel import SQLModel


class TaskProgressCreate(SQLModel):
    id_section:             int
    title:                  str
    modifies_progress:      bool | None = False
    progress_value:         int | None = 0


class TaskProgressRead(TaskProgressCreate):
    id:                     int


class TaskProgressUpdate(SQLModel):
    id_section:             int | None = None
    title:                  str | None = None
    modifies_progress:      bool | None = None
    progress_value:         int | None = None
