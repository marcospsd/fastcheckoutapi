FROM python:3.8

WORKDIR /code

COPY requeriments.txt .
RUN pip install -r requirements.txt

COPY . .