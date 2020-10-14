FROM python:3.8

COPY . /app

WORKDIR /app

RUN mkdir /db

# COPY requirements.txt /requirements.txt

RUN pip3 install -r /app/requirements.txt

CMD gunicorn --chdir app wsgi:app -w 1 --threads 1 -b 0.0.0.0:5000 --log-level=debug

RUN ls -la
