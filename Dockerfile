FROM python:3-alpine
RUN apk update

RUN mkdir /app
ADD requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
ADD . /app/