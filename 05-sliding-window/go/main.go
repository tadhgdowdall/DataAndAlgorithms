package main

import "fmt"

func main() {
	fmt.Println("=== Sliding Window Demos ===")

	// Best Time to Buy and Sell Stock
	fmt.Println("\n-- Best Time to Buy and Sell Stock --")
	fmt.Printf("maxProfits([7,1,5,3,6,4]) = %d\n", maxProfits([]int{7, 1, 5, 3, 6, 4}))
	fmt.Printf("maxProfits([7,6,4,3,1]) = %d\n", maxProfits([]int{7, 6, 4, 3, 1}))
}
