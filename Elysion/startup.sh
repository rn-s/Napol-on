#!/usr/bin/env bash

go run /usr/local/go/src/crypto/tls/generate_cert.go --host localhost
go run src/main.go