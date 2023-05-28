FROM python:3.9-slim-buster

# install package
RUN apt-get update \
    && apt-get install -y git

ADD requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /work
