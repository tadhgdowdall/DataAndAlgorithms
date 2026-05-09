package main

import "fmt"

func main() {
	fmt.Println("=== Stack Demos ===")

	// Valid Parentheses
	fmt.Println("\n-- Valid Parentheses --")
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
			fmt.Printf("Test %d passed: %s -> %t\n", i+1, tc.input, result)
		} else {
			fmt.Printf("Test %d failed: %s -> %t (expected %t)\n", i+1, tc.input, result, tc.expected)
		}
	}
}
