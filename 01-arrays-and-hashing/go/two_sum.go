package main

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
