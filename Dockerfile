FROM python:latest

LABEL \
    name="Sh00t" \
    author="Pavan <@pavanw3b>" \
    description="A Testing Environment for Manual Security Testers"


# Install some necessary things.
RUN apt-get update

# Copy files
COPY . /root/sh00t
WORKDIR /root/sh00t

RUN pip3 install -r requirements.txt

RUN pip3 install gunicorn

EXPOSE 8000

RUN chmod +x *.sh
RUN bash setup.sh
RUN bash run.sh

CMD ["gunicorn", "-b", "0.0.0.0:8000", "sh00t.wsgi:application", "--workers=1", "--threads=1", "--timeout=1800"]