FROM python:3-alpine

RUN apk add socat bash

ENV FLAG1=flag-L3sM4th5C3s7F4c1l3
ENV FLAG2=flag-UnP3uD3M4n1pu7ati0nDeRNG
COPY --chmod=711 entrypoint.sh /

WORKDIR /usr/src/app
COPY src/server1.py src/server2.py ./

CMD ["/entrypoint.sh"]