package main

import "fmt"

func main() {
	fmt.Println("=== Binary Search Demos ===")

	// Search 2D Matrix
	fmt.Println("\n-- Search 2D Matrix --")
	matrix := [][]int{
		{1, 3, 5, 7},
		{10, 11, 16, 20},
		{23, 30, 34, 60},
	}
	fmt.Printf("searchMatrix(matrix, 3) = %v\n", searchMatrix(matrix, 3))
	fmt.Printf("searchMatrix(matrix, 13) = %v\n", searchMatrix(matrix, 13))
}
