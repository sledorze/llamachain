FROM mcr.microsoft.com/devcontainers/python:3.12-bookworm

WORKDIR /workspaces/llamachain

COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt
