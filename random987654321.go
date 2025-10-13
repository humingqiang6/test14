package main

import (
	"fmt"
)

func printNumber(ch chan int, num int) {
	ch <- num
}

func main() {
	ch := make(chan int)

	for i := 1; i <= 10; i++ {
		go printNumber(ch, i)
	}

	for i := 1; i <= 10; i++ {
		fmt.Println(<-ch)
	}
}