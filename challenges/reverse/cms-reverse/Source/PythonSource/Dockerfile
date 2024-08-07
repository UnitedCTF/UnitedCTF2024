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
ENV PORT=9860
ENV SERVER_ID=cce13886a4e64875800f6ee80d5a7dfa
ENV FLAG3=FLAG3
ENV FLAG4=FLAG4
ENV TIME_BUFFER_NS=6_000_000_000

EXPOSE ${PORT} 

CMD python3 app.py