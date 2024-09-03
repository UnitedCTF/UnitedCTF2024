# syntax=docker/dockerfile:1
FROM golang

# Set destination for COPY
WORKDIR /app

# Download Go modules
COPY go.mod ./
RUN go mod download

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/reference/dockerfile/#copy
COPY *.go ./

# Build
RUN CGO_ENABLED=0 GOOS=linux go build -o /victim

ENV PORT=80
ENV PASSWORD=BW0mM85LgQhY2VcjDakO@l^HU

# Run
CMD ["/victim"]