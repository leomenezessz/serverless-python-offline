FROM node:15-buster-slim as base

WORKDIR /usr/app

RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get -y dist-upgrade && \
    apt-get install -y alien libaio1 wget python3 python3-pip git

COPY . .

RUN npm install -s
RUN pip3 install -r requirements.txt


