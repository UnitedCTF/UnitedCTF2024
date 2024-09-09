FROM golang:1.22-alpine

RUN mkdir /challenge
WORKDIR /challenge

COPY app/ .

RUN go build -o app 
RUN tar -xvf rockyou.txt.tar.gz && rm -rf rockyou.txt.tar.gz

EXPOSE 5000

CMD ["/challenge/app"]
