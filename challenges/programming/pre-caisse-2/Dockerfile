FROM python:3.11-alpine

WORKDIR /app

RUN apk update && \
    apk add --no-cache socat

COPY src/main.py .
COPY --chmod=711 entrypoint.sh .

EXPOSE 1337
CMD ["./entrypoint.sh"]