FROM python:3.6-alpine

LABEL \
    name="Sh00t" \
    author="Pavan <@pavanw3b>" \
    maintainer="Pavan <@pavanw3b>" \
    description="A Testing Environment for Manual Security Testers"

RUN mkdir sh00t
COPY . /root/sh00t
WORKDIR /root/sh00t
RUN pip3 install --upgrade pip && pip install -r requirements.txt
RUN python3 manage.py migrate && python3 reset.py first_timer
EXPOSE 8000
CMD ["sh", "scripts/run_setup.sh"]