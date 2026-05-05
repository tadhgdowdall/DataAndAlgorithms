package golang

import (
	"fmt"
	"math"
)

func twoPointer() {

}

// Problem: “Closest Pair Sum”
// You are given a sorted integer array nums and an integer target.
// Return the pair of indices (i, j) such that:
// i < j
// The sum nums[i] + nums[j] is closest to the target
// If multiple pairs have the same closest sum, return any one.

func closestPair(nums []int, target int) (int, int) {

	left, right := 0, len(nums)-1

	bestLeft, bestRight := 0, 1
	lowestDiff := abs(nums[left] + nums[right] - target)

	for left < right {
		sum := nums[left] + nums[right]

		// absolute difference
		diff := sum - target
		if diff < 0 {
			diff = -diff
		}

		// update best pair
		if diff < lowestDiff {
			lowestDiff = diff
			bestLeft = left
			bestRight = right
		}

		// move pointers based on sum
		if sum < target {
			left++
		} else if sum > target {
			right--
		} else {
			// exact match — can't get better than this
			return left, right
		}
	}

	return bestLeft, bestRight
}

func abs(x int) int {
	if x < 0 {
		return -x
	}
	return x
}

// Input: s = "loveleetcode", c = "e"
// Output: [3,2,1,0,1,0,0,1,2,2,1,0]
// Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
// The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
// The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
// For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is still the same: abs(4 - 3) == abs(4 - 5) = 1.
// The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.

func shortestToChar(s string, c byte) []int {

	n := len(s)

	answer := make([]int, n)

	// First pass: left to right
	prev := -n // something far away
	for i := 0; i < n; i++ {
		if s[i] == c {
			prev = i
		}
		answer[i] = i - prev
	}

	// Second pass: right to left
	prev = 2 * n // something far away
	for i := n - 1; i >= 0; i-- {
		if s[i] == c {
			prev = i
		}
		if prev-i < answer[i] {
			answer[i] = prev - i
		}
	}

	return answer
}
