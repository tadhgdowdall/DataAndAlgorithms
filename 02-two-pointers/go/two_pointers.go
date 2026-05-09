package main



func twoPointer() {
}

// Problem: "Closest Pair Sum"
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
