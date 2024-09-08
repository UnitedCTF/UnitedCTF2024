FROM python:3-alpine

RUN apk add socat bash

ENV FLAG1=flag-wwwwoo0ooOOOaAAa4ah
ENV FLAG2=flag-s3tTh30ryMuch
COPY --chmod=711 entrypoint.sh /

WORKDIR /usr/src/app
COPY src/server1.py src/server2.py ./

CMD ["/entrypoint.sh"]