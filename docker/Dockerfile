FROM python:3.12-slim

RUN apt update && apt -y install build-essential

RUN python -m pip install mypy

RUN mkdir /src

WORKDIR /src


