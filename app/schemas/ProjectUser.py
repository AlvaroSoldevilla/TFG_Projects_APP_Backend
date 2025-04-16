from sqlmodel import SQLModel


class ProjectUserCreate(SQLModel):
    id_user:        int
    id_project:     int
    id_role:        int | None = None


class ProjectUserRead(ProjectUserCreate):
    id:             int


class ProjectUserUpdate(SQLModel):
    id_user:        int | None = None
    id_project:     int | None = None
    id_role:        int | None = None
