From ubuntu:16.04
MAINTAINER Your name "navedshah@sbcons.net"
RUN apt-get update -y && \ 
    apt-get -y install python3 python3-venv python3-dev

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

COPY . /app

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]