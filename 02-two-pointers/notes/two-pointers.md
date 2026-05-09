# Two Pointers

## Key Concepts

- Two pointers moving towards each other (left/right)
- Two pointers moving in the same direction (fast/slow)
- One pointer per array (for merged/interleaved problems)

## When to Use

- Sorted arrays (two sum II)
- Palindrome checking
- Removing duplicates in-place
- Container with most water

## Common Patterns

1. **Opposite ends**: left at 0, right at n-1, move based on condition
2. **Same direction**: slow pointer for write, fast pointer for read

## Go Specifics

- No special syntax needed, just index tracking
- Be careful with string indexing; use `[]rune` for Unicode
