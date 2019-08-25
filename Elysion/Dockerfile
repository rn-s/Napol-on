FROM golang:latest

RUN go get github.com/labstack/echo/...

WORKDIR /app
ADD . /app

CMD ["go", "run", "src/main.go"]
