package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("Hello from the Day 35 multi-stage build demo")
	fmt.Printf("Runtime: %s/%s\n", runtime.GOOS, runtime.GOARCH)
}

