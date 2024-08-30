FROM php:8.2-fpm

RUN apt update -y && apt install git net-tools -y

RUN adduser user

USER user

RUN mkdir /home/user/app
COPY challenge/server /home/user/app

WORKDIR /home/user/app

USER root

RUN chmod +x ./composer.phar
RUN chown -R user:user /home/user/app/db/

USER user
RUN ./composer.phar install

ENV PORT=80
EXPOSE 80

CMD ["php", "main.php"]