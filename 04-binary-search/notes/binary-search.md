# Binary Search

## Key Concepts

- Divide search space in half each iteration
- Requires sorted data (or sorted-like structure)
- Classic: find target in sorted array

## Common Patterns

1. **Standard binary search**: find exact target
2. **Find boundary**: first/last occurrence
3. **Search space**: answer lies in a range (minimize maximum)
4. **2D matrix**: treat matrix as 1D sorted array

## Time & Space Complexity

- Time: O(log n)
- Space: O(1) iterative, O(log n) recursive

## Go Specifics

- Avoid overflow: `mid := left + (right-left)/2`
- Be careful with inclusive/exclusive bounds
