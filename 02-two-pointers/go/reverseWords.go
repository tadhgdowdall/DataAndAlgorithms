package main

import (
	"strings"
)

// Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
// Example 1:
// Input: s = "Let's take LeetCode contest"
// Output: "s'teL ekat edoCteeL tsetnoc"

func reverseWords(s string) string {

	left, right := 0, 0

	var output strings.Builder

	for right <= len(s) {

		// End of word OR end of string
		if right == len(s) || s[right] == ' ' {

			// Reverse current word
			for i := right - 1; i >= left; i-- {
				output.WriteByte(s[i])
			}

			// Preserve spaces
			if right != len(s) {
				output.WriteByte(' ')
			}

			// Move to next word
			left = right + 1
		}

		right++
	}

	return output.String()
}
