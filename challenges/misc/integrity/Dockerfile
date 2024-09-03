FROM alpine:latest

RUN apk add --no-cache g++ make libc-dev socat

WORKDIR /app

COPY src/main.cpp .
RUN g++ main.cpp -o integrity
RUN rm main.cpp

COPY entrypoint.sh .
RUN chmod +x entrypoint.sh

EXPOSE 1337
CMD ["./entrypoint.sh"]