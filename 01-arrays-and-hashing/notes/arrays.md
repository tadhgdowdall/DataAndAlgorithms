# Arrays & Hashing

## Key Concepts

- Arrays: contiguous memory, O(1) random access, O(n) insert/delete
- Hash Maps/Hash Sets: O(1) average lookup, insertion, deletion

## Common Patterns

1. **Use a Hash Set for uniqueness** - `Contains Duplicate`
2. **Use a Hash Map for frequency counting** - `Valid Anagram`
3. **Use a Hash Map for complement lookup** - `Two Sum`
4. **Use sum formula or XOR for missing elements** - `Missing Number`

## Time & Space Complexity

| Operation | Array | Hash Map |
|-----------|-------|----------|
| Access    | O(1)  | O(1)     |
| Search    | O(n)  | O(1)*    |
| Insert    | O(n)  | O(1)*    |
| Delete    | O(n)  | O(1)*    |

*Average case

## Go Specifics

- Maps: `make(map[keyType]valueType)`
- Check existence: `if val, ok := m[key]; ok { ... }`
- Maps are reference types
