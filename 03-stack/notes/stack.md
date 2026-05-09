# Stack

## Key Concepts

- LIFO: Last In, First Out
- Common operations: Push, Pop, Peek/Top
- Often used for parsing and matching problems

## When to Use

- Valid parentheses (matching brackets)
- Evaluate Reverse Polish Notation
- Daily Temperatures (monotonic stack)
- Min Stack

## Go Specifics

- No built-in stack; use slices:
  - Push: `stack = append(stack, val)`
  - Pop: `val := stack[len(stack)-1]; stack = stack[:len(stack)-1]`
- Check empty: `len(stack) == 0`
