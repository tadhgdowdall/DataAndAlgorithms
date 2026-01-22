package main

import "fmt"

func main() {
	// Test cases
	testCases := []struct {
		nums     []int
		target   int
		expected []int
	}{
		{[]int{2, 7, 11, 15}, 9, []int{0, 1}},
		{[]int{3, 2, 4}, 6, []int{1, 2}},
		{[]int{3, 3}, 6, []int{0, 1}},
	}

	for i, tc := range testCases {
		result := TwoSum(tc.nums, tc.target)
		fmt.Printf("Test case %d: nums=%v, target=%d -> result=%v\n", i+1, tc.nums, tc.target, result)
	}
}

func TwoSum(nums []int, target int) []int {
	seen := make(map[int]int) // Hash map
	for i, num := range nums {
		complement := target - num
		if j, ok := seen[complement]; ok {
			return []int{j, i}
		}
		seen[num] = i
	}
	return nil
}
