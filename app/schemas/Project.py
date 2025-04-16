from sqlmodel import SQLModel


class ProjectCreate(SQLModel):
    title:          str
    description:    str | None = ""


class ProjectRead(ProjectCreate):
    id:             int


class ProjectUpdate(SQLModel):
    title:          str | None = None
    description:    str | None = None
