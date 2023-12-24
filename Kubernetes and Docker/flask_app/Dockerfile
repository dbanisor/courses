FROM python:3.11

WORKDIR /app

COPY main.py /app

RUN pip install flask

COPY .. /app

CMD ["python", "./main.py"]
