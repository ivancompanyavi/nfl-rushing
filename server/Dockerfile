FROM python:3.9-slim-buster

RUN apt-get update && \
    apt-get -y install gcc && \
    apt-get clean

WORKDIR /usr/src/app

ENV FLASK_APP manage.py

COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY ./boot.sh /usr/src/app/boot.sh

COPY . /usr/src/app

EXPOSE 8000
