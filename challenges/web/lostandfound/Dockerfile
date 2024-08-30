FROM php:8.2-apache

WORKDIR /var/www/html

COPY --chown=root:root ./git.tar /var/www/html
RUN tar -xvf /var/www/html/git.tar && rm /var/www/html/git.tar
RUN echo "User-agent: *\nDisallow: .git" > /var/www/html/robots.txt 
