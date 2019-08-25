package main

import (
	"github.com/labstack/echo"
	"net/http"
)

func main() {
	e := echo.New()

	e.GET("/", func(c echo.Context) error {
		return c.JSON(http.StatusOK, map[string]string{"hello": "world"})
	})

	//e.Logger.Fatal(e.Start(":80"))
	e.Logger.Fatal(e.StartTLS(":443", "cert.pem", "key.pem"))
}