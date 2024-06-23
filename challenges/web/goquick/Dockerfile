FROM php:8.2-apache

RUN apt update && apt install -y dnsutils

ENV FLAG=FLAG-TH15_W41T1NG_L1N3_I5_R1D1CUL0U5
COPY --chmod=711 entrypoint.sh /

RUN rm -rf /var/www/html
ADD html /var/www/html

CMD ["/entrypoint.sh"]