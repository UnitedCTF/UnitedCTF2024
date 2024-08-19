FROM ubuntu

EXPOSE 80

RUN apt-get update

# Admin client simulation
ENV ADMIN_USER="admin"
ENV ADMIN_PASS="drakthull1"

RUN apt install bash curl -y
COPY admin_client/admin_login.sh /root/admin_login.sh
RUN chmod +x /root/admin_login.sh

# Webserver
ENV SESSION_KEY="2/BO0t4sH6+FN8r5ttut2KSn0zlSTR5NOHlGZZUyksvKf+jTWn+aj5OmNI+Hk85SawDOiltP7ZVC7nJCNrT1CA=="
ENV PORT="80"

RUN mkdir "/app"
COPY webserver /app/src
WORKDIR "/app/src"

RUN apt-get install golang -y
RUN go mod download
RUN go build -o /app/main .
RUN  chmod +x /app/main

# DB
ENV DB_HOST="localhost"
ENV DB_PORT="3306"
ENV DB_PASSWORD="7a3zcPnXe5Fx6HH8b6sh4zvaN"
ENV DB_USER="root"

RUN mkdir "/db"
COPY db /db

RUN apt-get install mariadb-server -y
RUN chmod +x /db/init_db.sh

# Entrypoint
COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh

CMD ["/entrypoint.sh"]