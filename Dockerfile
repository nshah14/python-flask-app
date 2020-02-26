FROM ubuntu:18.04

RUN apt-get update -y && \ 
    apt-get -y install python3  python3-pip  python3-dev libmysqlclient-dev

COPY . /microblog 
WORKDIR  /microblog

RUN pip3 install -r requirements.txt


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000
CMD flask run --host 0.0.0.0
