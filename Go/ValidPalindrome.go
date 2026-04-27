package main

import (
	"fmt"
	"strings"
)

// Given a string s, return true if it is a palindrome, otherwise return false.
// A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

// Input: s = "Was it a car or a cat I saw?"
// Output: true

func isPalindrome(s string) bool {

	left, right := 0, len(s)-1

	lowerCase := strings.ToLower(s)

	for left <= right {

		if lowerCase[left] != lowerCase[right] {
			return false
		}

		left++
		right--

	}

	return true

}

func isPalindromeRunes(s string) bool {

	runes := []rune(strings.ToLower(s))
	left, right := 0, len(runes)-1
	for left < right {
		if runes[left] != runes[right] {
			return false
		}
		left++
		right--
	}
	return true
}
