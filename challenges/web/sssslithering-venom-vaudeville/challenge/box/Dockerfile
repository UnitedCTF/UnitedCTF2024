FROM golang:latest

RUN apt-get update && apt-get install -y sudo ncat telnet gawk

RUN mkdir /app
WORKDIR /app
RUN mkdir log

COPY app/ .
COPY entrypoint.sh /

RUN touch log/master_logfile.log
RUN touch log/warning_logfile.log
RUN go get github.com/google/uuid
RUN go build -o app app.go 

RUN chmod 755 cleanup.sh /entrypoint.sh filter.awk app && \
    chmod 644 flag_67b88ce57ed45ec2d524e20cd6b19cf4.txt log/master_logfile.log log/warning_logfile.log

RUN useradd -m user
RUN chown user:user log/warning_logfile.log log/master_logfile.log

ENV PORT=80
# EXPOSE 80

CMD ["/entrypoint.sh"]
