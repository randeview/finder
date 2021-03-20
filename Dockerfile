FROM python:3.7-slim-buster
ENV PYTHONUNBUFFERED=1

RUN apt-get update \ 
    &&  apt-get -y install build-essential \
    && apt-get -y install gdal-bin


WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
