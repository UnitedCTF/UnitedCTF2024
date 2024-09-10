FROM alpine:latest

EXPOSE 22
ENV PASSWORD=anything1-slander-devourer-registrar

RUN apk update && \
    apk add --no-cache openssh

RUN cat > /usr/bin/sleep.sh <<EOF
#!/bin/sh

echo
echo "The bear is currently resting in this area:"
ip addr show 
echo
echo 🐻💤💤💤

sleep infinity
EOF
RUN chmod a+x /usr/bin/sleep.sh
RUN echo -n > /etc/motd

RUN adduser user -D -s "/usr/bin/sleep.sh" && \
    echo "user:$PASSWORD" | chpasswd

RUN sed -i 's/#PasswordAuthentication yes/PasswordAuthentication yes/' /etc/ssh/sshd_config
RUN sed -i 's/AllowTcpForwarding no/AllowTcpForwarding yes/' /etc/ssh/sshd_config
RUN ssh-keygen -A

CMD [ "/usr/sbin/sshd", "-D" ]