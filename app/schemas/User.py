from sqlmodel import SQLModel


class UserCreate(SQLModel):
    password:   str
    username:   str | None = None
    email:      str | None = None


class UserRead(SQLModel):
    id:         int
    username:   str | None = None
    email:      str | None = None


class UserUpdate(SQLModel):
    username:   str | None = None
    email:      str | None = None
    password:   str | None = None


class UserAuthenticate(SQLModel):
    password:   str
    username:   str
    email:      str


class UserEmail(SQLModel):
    email:      str


class RefreshToken(SQLModel):
    email:      str
    token:      str
