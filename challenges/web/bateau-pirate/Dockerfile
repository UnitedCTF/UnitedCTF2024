FROM python:3-alpine

WORKDIR /app

COPY src/ .

RUN pip install flask

EXPOSE 5000

CMD ["python", "app.py"]