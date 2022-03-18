FROM python:3.9
ENV PYTHONBUFFERED 1
LABEL maintainer "API FastCheckout"
COPY . /var/www
WORKDIR /var/www
RUN apt-get update && apt-get install -y gcc && apt-get install -y default-libmysqlclient-dev && pip install -r requeriments.txt && python manage.py migrate && python manage.py collectstatic
ENTRYPOINT gunicorn --bind 0.0.0.0:2000 fastcheckout.wsgi
EXPOSE 2000