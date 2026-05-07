package golang

import "fmt"

//Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

func hasDuplicate(nums []int) bool {

	seen := make(map[int]bool)

	for i := 0; i < len(nums); i++ {

		if seen[nums[i]] {
			return true
		}
		seen[nums[i]] = true
	}
	return false

}
