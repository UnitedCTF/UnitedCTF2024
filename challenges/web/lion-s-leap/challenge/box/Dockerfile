# Webserver
FROM golang:1.23-alpine AS builder

COPY webserver/src /root
WORKDIR "/root"

RUN go mod download
RUN go build -o /root/main .

FROM alpine
RUN apk add --no-cache curl

# Admin client simulation
ENV ADMIN_USER="admin"
ENV ADMIN_PASS="drakthull1"

# Entrypoint
RUN mkdir "/root/app"

WORKDIR /root/main
COPY --from=builder /root/main main
COPY /webserver/templates templates
COPY /webserver/static static

ENV SESSION_KEY="2/BO0t4sH6+FN8r5ttut2KSn0zlSTR5NOHlGZZUyksvKf+jTWn+aj5OmNI+Hk85SawDOiltP7ZVC7nJCNrT1CA=="
ENV PORT="80"
ENV DB_HOST="mariadb"
ENV DB_PORT="3306"
ENV DB_PASSWORD="GrpLJfnipshQMRBe0"
ENV DB_USER="user"

EXPOSE ${PORT}

CMD ["./main"]