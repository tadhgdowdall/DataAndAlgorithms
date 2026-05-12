package main

// LeetCode 283: Move Zeroes
// Given an integer array nums, move all 0's to the end of it while
// maintaining the relative order of the non-zero elements.
// You must do this in-place without making a copy of the array.
//
// Example:
// Input: [0, 1, 0, 3, 12]
// Output: [1, 3, 12, 0, 0]

func moveZeroes(nums []int) {
	slow := 0

	for fast := 0; fast < len(nums); fast++ {
		if nums[fast] != 0 {
			nums[slow], nums[fast] = nums[fast], nums[slow]
			slow++
		}
	}

}
