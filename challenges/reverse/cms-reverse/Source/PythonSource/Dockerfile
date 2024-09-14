FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser
RUN --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python3 -m pip install -r requirements.txt

USER appuser

COPY . .
ENV PORT=10000
ENV SERVER_ID=cce13886a4e64875800f6ee80d5a7dfa
ENV FLAG3="flag-WQ8TZXL5V7P1BK9QR7ZQ2JPXLMN4V5QW"
ENV FLAG4="flag-Q8T3R6A5ZX7P9JFR2C3DZ8JKR6YA2PXLM"
ENV TIME_BUFFER_NS=6_000_000_000

EXPOSE ${PORT} 

CMD python3 app.py
