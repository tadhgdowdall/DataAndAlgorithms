package main

import "fmt"

func main() {
	fmt.Println("=== Two Pointers Demos ===")

	// Valid Palindrome
	fmt.Println("\n-- Valid Palindrome --")
	fmt.Printf("isPalindrome(\"racecar\") = %v\n", isPalindrome("racecar"))
	fmt.Printf("isPalindrome(\"hello\") = %v\n", isPalindrome("hello"))

	// Closest Pair
	fmt.Println("\n-- Closest Pair --")
	nums := []int{1, 4, 5, 7, 10}
	target := 12
	i, j := closestPair(nums, target)
	fmt.Printf("closestPair(%v, %d) = indices (%d, %d), sum = %d\n", nums, target, i, j, nums[i]+nums[j])

	// Shortest To Char
	fmt.Println("\n-- Shortest To Char --")
	result := shortestToChar("loveleetcode", 'e')
	fmt.Printf("shortestToChar(\"loveleetcode\", 'e') = %v\n", result)
}
