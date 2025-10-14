package main

import (
	"fmt"
)

func printNumber(ch chan int, num int) {
	ch <- num // Send the number to the channel
}

func main() {
	ch := make(chan int, 10) // Create a channel with buffer size 10

	// Start 10 goroutines
	for i := 1; i <= 10; i++ {
		go printNumber(ch, i)
	}

	// Collect the results
	for i := 1; i <= 10; i++ {
		num := <-ch // Receive the number from the channel
		fmt.Println(num)
	}
}