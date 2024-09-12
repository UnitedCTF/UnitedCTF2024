FROM ubuntu:latest

ENV PASSWORD=traps-sizably-jogger-scrimmage2

RUN apt-get update && apt-get install -y sudo ncat telnet iputils-ping openssh-server nmap net-tools

RUN useradd -m user
RUN echo "user:$PASSWORD" | chpasswd
RUN mkdir /var/run/sshd

# Allow password authentication
RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/AllowTcpForwarding no/AllowTcpForwarding yes/' /etc/ssh/sshd_config

# Expose SSH port
EXPOSE 22

CMD ["/usr/sbin/sshd", "-D"]
