FROM php:7.4-apache

COPY index.php /var/www/html/index.php
COPY php.ini /usr/local/etc/php/

RUN mkdir -p /var/lib/php/sessions \
    && chmod 1733 /var/lib/php/sessions \
    && chown www-data:www-data /var/lib/php/sessions

RUN echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_4a7d1ed4144674e4033ac29ccb8653d9b \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_15a1588c37430224440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_25a1588c37430024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_35a1588c37493024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_45a1588c37423024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_55a1588c37463024440677c186380d9b3 \
    && echo "user_role|s:5:\"admin\";" > /var/lib/php/sessions/sess_65a1588c37413024440677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_75a1588c37430244940677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_85a1588c37430244540677c186380d9b3 \
    && echo "user_role|s:4:\"user\";" > /var/lib/php/sessions/sess_95a1588c37430241440677c186380d9b3

RUN chown www-data:www-data /var/lib/php/sessions/*

WORKDIR /
COPY setup.sh .
RUN chmod +x setup.sh && ./setup.sh
RUN rm setup.sh

RUN touch '.flag-HoHoPHPOupsiiii'

EXPOSE 80

CMD ["apache2-foreground"]
