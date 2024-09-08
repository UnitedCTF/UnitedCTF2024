FROM golang

# Set destination for COPY
WORKDIR /app

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/reference/dockerfile/#copy
COPY . ./

# Build
RUN go mod download
RUN go build -o webserver .
RUN chmod +x webserver

ENV PORT=80
EXPOSE $PORT

ENV SESSION_KEY="/nHBGyd8CnFqp3od9seRbwnti+1EZAmeYspgZr+oBn8="

# Run
CMD ["/app/webserver"]