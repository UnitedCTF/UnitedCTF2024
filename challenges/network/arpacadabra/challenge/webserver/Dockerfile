FROM golang:alpine3.20 AS build

# Set destination for COPY
WORKDIR /app

# Copy the source code. Note the slash at the end, as explained in
# https://docs.docker.com/reference/dockerfile/#copy
COPY . ./

# Build
RUN go mod download
RUN CGO_ENABLED=0 GOOS=linux go build -o webserver


FROM scratch
COPY --from=build /app/webserver /webserver
COPY --from=build /app/static /static
COPY --from=build /app/templates /templates

ENV SESSION_KEY="/nHBGyd8CnFqp3od9seRbwnti+1EZAmeYspgZr+oBn8="
ENV PORT=80
EXPOSE $PORT

ENTRYPOINT ["/webserver"]