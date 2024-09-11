FROM alpine:latest

EXPOSE 22

RUN apk --update add bash \
    iproute2 \
    less \
    vim \
    iputils \
    tcpdump \
    curl \
    scapy \
    ipython \
    tmux \
    openssh \
    sudo

RUN adduser -D user -s /bin/bash
RUN adduser user wheel
RUN echo '%wheel ALL=(ALL) ALL' > /etc/sudoers.d/wheel

ENV PASSWORD=steadying-cursor-sulfide-rudder4
RUN ssh-keygen -A
RUN echo "user:$PASSWORD" | chpasswd
RUN mkdir /var/run/sshd

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/AllowTcpForwarding no/AllowTcpForwarding yes/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]
