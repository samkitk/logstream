# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /python-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
RUN apt-get update 
RUN apt-get install vim nano -y
COPY . .

CMD [ "python3", "server.py"]