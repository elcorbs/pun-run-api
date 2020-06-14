FROM python:3-alpine

WORKDIR /app

RUN \
   # install postgres-libs
   #install gcc