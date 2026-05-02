package golang

import (
	"fmt"
)

func main() {

}

func twoSum(nums []int, target int) []int {

	for i := 0; i < len(nums); i++ {
		if nums[i]+nums[i+1] == target {
			return []int{nums[i], nums[i+1]}
		}

	}
	return []int{0, 0}

}
