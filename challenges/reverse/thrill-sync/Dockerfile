FROM php:8.2-fpm

RUN apt update -y && apt install git net-tools -y

RUN adduser user

USER user

RUN mkdir /home/user/app
COPY challenge/server/ /home/user/app

WORKDIR /home/user/app

USER root

RUN chmod +x ./composer.phar

USER user
RUN ./composer.phar install

ENV PORT=8081
EXPOSE 8081

#CMD ["php", "main.php"]
CMD ["tail", "-f", "/dev/null"]