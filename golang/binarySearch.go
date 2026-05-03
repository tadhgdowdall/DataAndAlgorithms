package golang

// You are given an m x n 2-D integer array matrix and an integer target.
// Each row in matrix is sorted in non-decreasing order.
// The first integer of every row is greater than the last integer of the previous row.
// Return true if target exists within matrix or false otherwise.

func searchMatrix(matrix [][]int, target int) bool {

	m := len(matrix)
	n := len(matrix[0])

	left := 0
	right := m*n - 1

	for left <= right {
		mid := left + (right-left)/2

		row := mid / n
		col := mid % n
		val := matrix[row][col]

		if val == target {
			return true
		} else if val < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}

	return false

}
