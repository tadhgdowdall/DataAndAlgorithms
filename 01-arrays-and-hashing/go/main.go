package main

import "fmt"

func main() {
	fmt.Println("=== Arrays & Hashing Demos ===")

	// Two Sum
	fmt.Println("\n-- Two Sum --")
	fmt.Printf("TwoSum([2,7,11,15], 9) = %v\n", TwoSum([]int{2, 7, 11, 15}, 9))
	fmt.Printf("TwoSum([3,2,4], 6) = %v\n", TwoSum([]int{3, 2, 4}, 6))

	// Contains Duplicate
	fmt.Println("\n-- Contains Duplicate --")
	fmt.Printf("hasDuplicate([1,2,3,1]) = %v\n", hasDuplicate([]int{1, 2, 3, 1}))
	fmt.Printf("hasDuplicate([1,2,3,4]) = %v\n", hasDuplicate([]int{1, 2, 3, 4}))
}
