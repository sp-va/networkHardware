FROM python:3.13-slim

RUN apt-get update && apt-get install -y gcc libmariadb-dev

RUN pip install --upgrade pip && pip install poetry

WORKDIR /app

COPY pyproject.toml poetry.lock* /app/

RUN poetry config virtualenvs.create false && poetry install --no-interaction --no-ansi

COPY . /app/

EXPOSE 8080

# Команда запуска сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8080"]
