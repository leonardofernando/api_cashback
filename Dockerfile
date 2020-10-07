FROM python:3.8

COPY . /app
WORKDIR /app

COPY requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

# CMD gunicorn --chdir app wsgi:app -w 2 --threads 2 -b 0.0.0.0:5000 --log-level=error

