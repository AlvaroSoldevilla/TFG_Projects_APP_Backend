
# TFG Projects App - Backend

API REST desarrollada con FastAPI como parte del Trabajo de Fin de Grado en Desarrollo de Aplicaciones Multiplataforma. Este servidor gestiona la lógica de negocio, persistencia de datos y autenticación para la aplicación cliente desarrollada en .NET MAUI.

Para información sobre el cliente, visitar el siguiente enlace:

[TFG_Projects_APP_Frontend](https://github.com/AlvaroSoldevilla/TFG_Projects_APP_Frontend)
## Características

- Autenticación y autorización mediante tokens JWT
- Gestión de usuarios y permisos por proyecto
- Soporte para tareas, tableros y mapas conceptuales
- Endpoints organizados por módulos (usuarios, componentes, proyectos…)
- Documentación automática con Swagger
- Pruebas unitarias con pytest y dependencias mockeadas
- Base de datos relacional con SQLModel y soporte para SQLite y PostgreSQL


## Tecnologías usadas

- **FastAPI** — Framework web moderno y asíncrono
- **SQLModel** — ORM basado en SQLAlchemy y Pydantic
- **Pytest** — Framework de testing
- **Docker** — Contenedorización para desarrollo y despliegue
- **Uvicorn** — Servidor ASGI para aplicaciones FastAPI


## Instalación

Puedes acceder a una versión desplegada mediante el siguente enlace.

http://vms.iesluisvives.org:25004

Para clonar el repositorio:

```bash
    git clone https://github.com/AlvaroSoldevilla/TFG_Projects_APP_backend
    cd TFG_Projects_APP_Backend
```

Para ejecutar la aplicación:

```bash
    pip install -r requirements.txt
```

Instalar dependencias:

```bash
    python -m venv venv
    venv\Scripts\activate
```

Ejecutar el servidor:

```bash
    uvicorn app.main:app --reload
```

Por defecto, la API estará disponible en:

http://localhost:8000


## Montar con Docker

Para montar la aplicación con Docker:

### Montar con Sqlite

Sqlite es una buena opción para individuos o equipos pequeños que quieran una base de datos ligera.

Lo primero es modificar el fichero .env y establecer las variables de entorno

```
DATABASE_TYPE=sqlite                        # Tipo de la base de datos, no modificar
POSTGRES_USER=your_postgres_user            # Ignorar si se usa sqlite
POSTGRES_PASSWORD=your_postgres_password    # Ignorar si se usa sqlite
POSTGRES_DB=your_postgres_db                # Ignorar si se usa sqlite
DB_HOST=db                                  # Nombre del fichero de la base de datos
DEBUG=True                                  # Determina si se inicia en modo DEBUG
SECRET=your_secret_token_password           # Clave de cifrado de los tokens JWT
ALGORITHM=HS256                             #Algoritmo de cifrado de los tokens JWT
```

Una vez hecho eso, se monta la imagen y el servidor estaría funcionando.

```bash
    docker build -t nombre_de_la_imagen:tag . 
    docker run --name nombre_del_contenedor -p 8080:8000 -it nombre_de_la_imagen:tag
```

### Montar con PostgreSQL

PostgreSQL es mejor para equipos que prevean una mayor carga de peticiones y necesiten una base de datos más robusta.

Similar a Sqlite, lo primero es modificar las variables de entorno, usando el Dockerfile proporcionado o creando uno nuevo, asegurandose de que las variables relacionadas con la base de datos son las mismas en ambos contenedores:

```bash
version: "3.8"

services:
  api:
    build:
      context: .
    depends_on:
      - db
    ports:
      - "25004:8000"
    environment:
      - DATABASE_TYPE=postgres
      - POSTGRES_PASSWORD=productsapi
      - POSTGRES_USER=productsapi
      - POSTGRES_DB=productsapi
      - DB_HOST=db
      - SECRET=your_secret_password
      - ALGORITHM=HS256
    networks:
      - internal_net
  db:
    image: postgres:15
    ports:
      - 5432:5432
    environment:
      - POSTGRES_PASSWORD=productsapi
      - POSTGRES_USER=productsapi
      - POSTGRES_DB=productsapi
    networks:
      - internal_net

networks:
  internal_net:
    driver: bridge
```

Una vez hecho eso, al ejecutar el siguiente comando, el servidor empezará a funcionar y estará listo para recibir peticiones:

```bash
    docker compose up -d
```


## Preguntas frecuentes



