FROM golang:latest

COPY startup.sh /startup.sh
RUN go get github.com/labstack/echo/... && chmod 744 /startup.sh

WORKDIR /app
ADD . /app

CMD ["/startup.sh"]