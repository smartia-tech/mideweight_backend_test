# base image
FROM python:3.8


# set environment variables
ENV PYTHONUNBUFFERED 1

RUN mkdir /smartia


WORKDIR /smartia


COPY requirements.txt /smartia/


RUN pip3 install --upgrade pip


# installing all dependencies
RUN pip3 install -r requirements.txt


COPY . /smartia/
