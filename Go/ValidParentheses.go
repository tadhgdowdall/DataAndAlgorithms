package main

import (
	"fmt"
)

func isValid(s string) bool {
	stack := []rune{}
	mapping := map[rune]rune{
		')': '(',
		'}': '{',
		']': '[',
	}

	for _, char := range s {
		if char == '(' || char == '{' || char == '[' {
			stack = append(stack, char)
		} else {
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if top != mapping[char] {
				return false
			}
		}
	}

	return len(stack) == 0
}

func main() {
	// Test cases
	testCases := []struct {
		input    string
		expected bool
	}{
		{"()", true},
		{"()[]{}", true},
		{"(]", false},
		{"([)]", false},
		{"{[]}", true},
		{"", true},
		{"[", false},
		{"}", false},
	}

	for i, tc := range testCases {
		result := isValid(tc.input)
		if result == tc.expected {
			fmt.Printf("Test case %d passed: %s -> %t\n", i+1, tc.input, result)
		} else {
			fmt.Printf("Test case %d failed: %s -> %t (expected %t)\n", i+1, tc.input, result, tc.expected)
		}
	}
}
