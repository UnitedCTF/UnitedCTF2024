FROM golang:latest

RUN mkdir /challenge
WORKDIR /challenge

COPY app/ .

RUN go build -o app app.go 
RUN tar -xvf rockyou.txt.tar.gz

EXPOSE 5000

CMD ["/challenge/app"]
