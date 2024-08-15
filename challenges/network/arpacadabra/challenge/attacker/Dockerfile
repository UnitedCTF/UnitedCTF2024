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
    openssh

ENV PASSWORD=steadying-cursor-sulfide-rudder4
RUN ssh-keygen -A
RUN echo "root:$PASSWORD" | chpasswd
RUN mkdir /var/run/sshd

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

CMD ["/usr/sbin/sshd", "-D"]
