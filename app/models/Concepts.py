from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class Concepts(SQLModel, table=True):
    id:                 int | None = Field(default=None, primary_key=True)
    id_project:         int | None = Field(default=None, foreign_key="projects.id")
    title:              str | None = None
    description:        str | None = None

    project:            Optional["Projects"] = Relationship(back_populates="concepts")
    concept_boards:     Optional[list["ConceptBoards"]] = Relationship(back_populates="concept")
