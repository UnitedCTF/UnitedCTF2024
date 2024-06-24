FROM debian:bookworm AS builder

RUN apt update && apt install -y git libtool automake build-essential libssl-dev libc-ares-dev

RUN git clone https://github.com/curl/curl
WORKDIR /curl

RUN libtoolize --force && \
    aclocal && \
    autoheader && \
    automake --force-missing --add-missing && \
    autoconf

RUN ./configure --with-openssl --enable-ares && \
    make && \
    make install


FROM php:8.2-apache

RUN apt update && apt install -y dnsutils libc-ares-dev

ENV FLAG=flag-C3tteL1gn3DAtt3nt3EstR1d1cul3m3n7L0ngu3
COPY --chmod=711 entrypoint.sh /

COPY --from=builder /usr/local/bin/curl /usr/bin/curl
COPY --from=builder /usr/local/lib/libcurl.so.4 /usr/lib/x86_64-linux-gnu/libcurl.so.4

RUN rm -rf /var/www/html
ADD --chown=www-data src /var/www/html

CMD ["/entrypoint.sh"]