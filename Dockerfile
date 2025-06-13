FROM python:3.12.9-slim

WORKDIR /code

COPY .env /code/.env
COPY requirements.txt /code/requirements.txt
COPY ./app /code/app

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install psycopg2-binary

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000","--reload"]

USER user