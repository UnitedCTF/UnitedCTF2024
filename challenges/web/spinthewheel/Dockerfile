FROM python:3.11-slim-bookworm

WORKDIR /usr/src/app

RUN pip install --no-cache-dir flask

COPY src/ .

CMD ["python", "-m", "flask", "run", "--host=0.0.0.0"]