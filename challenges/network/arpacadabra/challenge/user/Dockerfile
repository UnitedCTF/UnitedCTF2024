# syntax=docker/dockerfile:1
FROM golang:alpine3.20 AS build

# Set destination for COPY
WORKDIR /app

# Download Go modules
COPY go.mod ./
RUN go mod download

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/reference/dockerfile/#copy
COPY *.go ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o victim


FROM scratch

ENV USERNAME=admin
ENV PASSWORD=BW0mM85LgQhY2VcjDakO@l^HU
ENV WEBSERVER_URL=http://webserver:80

COPY --from=build /app/victim /victim
ENTRYPOINT ["/victim"]
