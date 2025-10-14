package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printNumber(num int) {
	defer wg.Done() // Notify that the goroutine is finished
	fmt.Println(num)
}

func main() {
	for i := 1; i <= 10; i++ {
		wg.Add(1) // Increment the WaitGroup counter
		go printNumber(i)
	}

	wg.Wait() // Wait for all goroutines to finish
}