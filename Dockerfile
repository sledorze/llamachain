FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
