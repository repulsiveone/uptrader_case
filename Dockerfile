FROM python:3.10-slim-buster

ENV PYTHONUNBUFFERED 1

WORKDIR /uptrader

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc libpq-dev && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000