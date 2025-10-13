package main

import (
	"fmt"
	"time"
)

func printNumbers() {
	for i := 1; i <= 10; i++ {
		fmt.Println(i)
		time.Sleep(100 * time.Millisecond) // 添加短暂延迟以观察并发效果
	}
}

func main() {
	// 启动一个Go协程来执行printNumbers函数
	go printNumbers()

	// 主协程等待一段时间，确保其他协程有时间执行
	time.Sleep(2 * time.Second)
}