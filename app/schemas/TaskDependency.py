from sqlmodel import SQLModel


class TaskDependencyCreate(SQLModel):
    id_task:            int
    id_depends_on:      int
    unlock_at:          int | None = 100


class TaskDependencyRead(TaskDependencyCreate):
    id:                 int


class TaskDependencyUpdate(SQLModel):
    id_task:            int | None = None
    id_depends_on:      int | None = None
    unlock_at:          int | None = None
