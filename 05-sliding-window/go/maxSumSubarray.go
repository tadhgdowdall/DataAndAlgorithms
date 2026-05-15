package main

import (
	"fmt"
)

// Maximum Sum Subarray of Size K
// Given an integer slice nums and an integer k, find the maximum sum of any contiguous subarray of size k.

// Input:
// nums = [2, 1, 5, 1, 3, 2]
// k = 3
// Output:
// 9
func maxSumSubarray(nums []int, k int) int {

	// So you are just checking a subarray of 3 at any one time and calculating the sum
	windowSum := 0
	for i := 0; i < k; i++ {
		windowSum += nums[i]
	}

	// Start maxSum with the first window's sum
	maxSum := windowSum

	// Slide the window across the array
	for right := k; right < len(nums); right++ {
		// Add incoming element
		windowSum += nums[right]

		// Subtract outgoing element
		windowSum -= nums[right-k]

		// Update max if needed
		if windowSum > maxSum {
			maxSum = windowSum
		}
	}

	return maxSum
}
