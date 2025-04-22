from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class ConceptBoards(SQLModel, table=True):
    __tablename__ = "concept_boards"

    id:             int | None = Field(default=None, primary_key=True)
    id_concept:     int | None = Field(default=None, foreign_key="concepts.id")
    id_parent:      int | None = Field(default=None, foreign_key="concept_boards.id")

    concept:        Optional["Concepts"] = Relationship(back_populates="concept_boards")
    parent: Optional["ConceptBoards"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "ConceptBoards.id"}
    )
    children:       Optional[list["ConceptBoards"]] = Relationship(back_populates="parent")
    components:     Optional[list["Components"]] = Relationship(back_populates="board")
