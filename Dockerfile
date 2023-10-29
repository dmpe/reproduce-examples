FROM python:latest

SHELL ["/bin/bash", "-o", "pipefail", "-c"]
ENV DEBIAN_FRONTEND=noninteractive

ENV LANG C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1

RUN apt update 
RUN apt install -y nano tree && mkdir -p /home/ubuntu/project/code
RUN python3 -m venv /home/ubuntu/project 
RUN . /home/ubuntu/project/bin/activate
ENV PATH="/home/ubuntu/project/bin:${PATH}"

WORKDIR /home/ubuntu/project
COPY requirenments.txt .
RUN pip install -r requirenments.txt

