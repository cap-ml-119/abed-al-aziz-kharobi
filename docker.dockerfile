FROM python:3.9-slim-buster

WORKDIR /app


COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY . .
EXPOSE 7000

CMD [ "python", "main.py"]