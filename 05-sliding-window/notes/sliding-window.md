# Sliding Window

## Key Concepts

- Subarray/substring problems
- Window expands/contracts based on condition
- Two pointers with dynamic distance

## When to Use

- Best Time to Buy and Sell Stock
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Fixed-size window problems

## Common Patterns

1. **Dynamic window**: expand right, contract left when invalid
2. **Fixed window**: slide a window of size k

## Go Specifics

- Use two indices (left, right) over slices
- Map for character frequency in window
