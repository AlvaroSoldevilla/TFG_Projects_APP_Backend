from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class ConceptBoards(SQLModel, table=True):
    __tablename__ = "concept_boards"

    id:             int | None = Field(default=None, primary_key=True)
    id_concept:     int | None = Field(default=None, foreign_key="concepts.id")
    id_parent:      int | None = Field(default=None, foreign_key="concept_boards.id")
    name:           str | None

    concept:        Optional["Concepts"] = Relationship(back_populates="concept_boards")
    components:     Optional[list["Components"]] = Relationship(back_populates="board", cascade_delete=True)
