package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func is_prime(num int) bool {
	if num < 2 {
		return false
	}
	for i := 2; i*i <= num; i++ {
		if num%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Print("Enter the limit n: ")
	reader := bufio.NewReader(os.Stdin)
	limitInput, _ := reader.ReadString('\n')
	limitInput = limitInput[:len(limitInput)-1]
	n, _ := strconv.Atoi(limitInput)

	fmt.Println()

	for i := 2; i < n; i++ {
		if is_prime(i) {
			fmt.Printf("%d ", i)
		}
	}
	fmt.Println()
}
