FROM python:3.9-slim

WORKDIR /app

COPY poetry.lock pyproject.toml .

RUN pip3 install --upgrade pip

RUN pip3 install poetry

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

RUN pip3 install -r requirements.txt --no-cache-dir

COPY . .