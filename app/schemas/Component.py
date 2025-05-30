from sqlmodel import SQLModel


class ComponentCreate(SQLModel):
    id_board:   int
    id_type:    int
    title:      str

    id_parent:  int | None = None
    pos_x:      float | None = 0
    pos_y:      float | None = 0
    content:    str | None = ""


class ComponentRead(ComponentCreate):
    id:         int


class ComponentUpdate(SQLModel):
    id_board:   int | None = None
    id_type:    int | None = None
    title:      str | None = None

    id_parent:  int | None = None
    pos_x:      float | None = None
    pos_y:      float | None = None
    content:    str | None = None
