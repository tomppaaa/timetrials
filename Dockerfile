# syntax=docker/dockerfile:1
FROM python:alpine
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "gunicorn", "-w", "4", "flaskr:app", "-b", "0.0.0.0:5000", "--access-logfile", "-", "--error-logfile", "-"]
# CMD [ "gunicorn", "-w", "4", "flaskr:app", "-b", "0.0.0.0:5000"]
