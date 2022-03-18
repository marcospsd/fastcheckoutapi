FROM python:3.9-alpine
LABEL maintainer "API FastCheckout <mdias@dinizvitoria.com.br>"
COPY . /var/www
WORKDIR /var/www
RUN apk update && apk add zlib-dev jpeg-dev gcc musl-dev && pip install -r requeriments.txt && python manage.py migrate && python manage.py collectstatic
ENTRYPOINT gunicorn -bind 0.0.0.0:2000 fastcheckout.wsgi
EXPOSE 2000