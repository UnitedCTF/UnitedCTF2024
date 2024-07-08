FROM node:20

RUN apt update && \
      apt install -y socat

WORKDIR /app
COPY --chown=root:root ./challenge.js /app/challenge.js
RUN chmod 755 /app/challenge.js

COPY --chown=root:root ./flag.txt /app/flag.txt

USER node
EXPOSE 1234
ENTRYPOINT [ "socat", "-v", "tcp-listen:1234,reuseaddr,fork", "exec:/app/challenge.js" ]
