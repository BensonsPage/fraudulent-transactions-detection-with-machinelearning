# syntax=docker/dockerfile:1

# docker build -t /fraudulent-transactions-detection-app:latest .

FROM python:3.10

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

COPY . .

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]

