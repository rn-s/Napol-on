package main

import (
	"cloud.google.com/go/firestore"
	"context"
	"fmt"
	"github.com/labstack/echo"
	"google.golang.org/api/iterator"
	"log"
	"net/http"
)

func main() {
	e := echo.New()
	http.Handle("/", e)

	e.GET("/", func(c echo.Context) error {

		projectID := "****"
		ctx := context.Background()
		client, err := firestore.NewClient(ctx, projectID)
		if err != nil {
			log.Fatalf("Failed to create client: %v", err)
		}

		iter := client.Collection("shop").Documents(ctx)
		for {
			doc, err := iter.Next()
			if err == iterator.Done {
				break
			}
			if err != nil {
				log.Fatalf("Failed to iterate: %v", err)
			}
			fmt.Println(doc.Data())
		}
		defer client.Close()
		return c.String(http.StatusOK, "Hello, World!")
	})

	e.Logger.Fatal(e.Start(":8080"))
}
