FROM ubuntu:latest

EXPOSE 22

ENV PASSWORD=marbled-casino-zodiac-composer

RUN apt-get update && apt-get install -y sudo ncat telnet iputils-ping openssh-server sqlmap curl net-tools vim

RUN useradd -m user
RUN echo "user:$PASSWORD" | chpasswd
RUN mkdir /var/run/sshd

# Allow password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]
