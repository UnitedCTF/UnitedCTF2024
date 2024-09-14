FROM php:8.2-apache

RUN apt update && \
      apt install -y p7zip-full

COPY --chown=root:root ./html/ /var/www/html 
RUN mkdir -p /var/www/html/websites
RUN chmod 1777 /var/www/html/websites

COPY --chown=root:root ./healthcheck.sh /healthcheck.sh
HEALTHCHECK --interval=5m --timeout=30s --start-period=30s --start-interval=5s --retries=3 \
  CMD [ "/healthcheck.sh" ]

RUN chmod +x /healthcheck.sh /var/www/html/scripts/*