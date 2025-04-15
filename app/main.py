from fastapi import FastAPI
from app.db.session import engine, fill_base_data
from sqlmodel import SQLModel

app = FastAPI()

# Registrar las rutas


# Crear tablas en la base de datos si no existen
def init_db():
    SQLModel.metadata.create_all(engine)
    fill_base_data()


init_db()
