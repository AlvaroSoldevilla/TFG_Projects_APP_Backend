from sqlmodel import SQLModel


class ConceptCreate(SQLModel):
    id_project:     int
    id_first_board: int
    title:          str
    description:    str | None = ""


class ConceptRead(ConceptCreate):
    id:             int


class ConceptUpdate(SQLModel):
    id_project:     int | None = None
    id_first_board: int | None = None
    title:          str | None = None
    description:    str | None = None
