FROM python:3.6-alpine

LABEL \
    name="Sh00t" \
    author="Pavan <@pavanw3b>" \
    maintainer="Pavan <@pavanw3b>" \
    description="A Testing Environment for Manual Security Testers"


# Copy files
COPY . /root/sh00t
WORKDIR /root/sh00t

RUN pip3 install --upgrade pip

RUN pip install -r requirements.txt

EXPOSE 8000

RUN python3 manage.py migrate
RUN python3 scripts/createsuperuser.py
RUN python3 reset.py first_timer

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]