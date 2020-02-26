FROM alpine:3.11

RUN apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev  libc-dev && \
    apk add --no-cache --update python3 && \
    pip3 install --upgrade pip setuptools
# RUN pip3 install pendulum service_identity
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY . /microblog 
WORKDIR  /microblog

RUN pip3 install  mysqlclient  
RUN pip3 install -r requirements.txt


ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

EXPOSE 5000
CMD flask run --host 0.0.0.0
