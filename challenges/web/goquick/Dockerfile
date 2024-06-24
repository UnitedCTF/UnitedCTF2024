FROM php:8.2-apache

RUN apt update && apt install -y dnsutils libc-ares-dev zip

ENV FLAG=flag-C3tteL1gn3DAtt3nt3EstR1d1cul3m3n7L0ngu3
COPY --chmod=711 entrypoint.sh /

RUN rm -rf /var/www/html
ADD --chown=www-data src /var/www/html

CMD ["/entrypoint.sh"]