FROM ubuntu:18.04

LABEL \
    name="Sh00t" \
    author="Pavan <@pavanw3b>" \
    maintainer="Pavan <@pavanw3b>" \
    description="A Testing Environment for Manual Security Testers"


RUN apt-get update -y && apt-get install -y \
    python3-pip \
    python3-dev \
    nginx


# Copy files
COPY . /root/sh00t
WORKDIR /root/sh00t

RUN pip3 install --upgrade pip
RUN pip3 install virtualenv
RUN virtualenv env
RUN /bin/bash -c "source env/bin/activate"

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python3 manage.py migrate