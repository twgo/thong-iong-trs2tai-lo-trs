FROM ubuntu:16.04
MAINTAINER sih4sing5hong5

RUN apt-get update -qq
RUN apt-get install -y python3 virtualenv g++ python3-dev git libpq-dev postgresql postgresql-contrib make

# Switch locale
RUN locale-gen zh_TW.UTF-8
ENV LC_ALL zh_TW.UTF-8

RUN apt-get install -y python3-pip
RUN pip3 install --upgrade pip
RUN pip3 install Django
RUN pip3 install tai5-uan5-gian5-gi2-kang1-ku7
RUN pip3 install gunicorn

EXPOSE 8000

COPY . .

CMD gunicorn tsuan2.wsgi -b 0.0.0.0:8000 -w 4 --log-level DEBUG

