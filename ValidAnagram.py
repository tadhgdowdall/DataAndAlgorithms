def is_anagram_sorting(s, t):
    """
    Sorting Approach - O(n log n) time, O(1) space
    Check if two strings are anagrams by sorting both strings
    """
    # Your solution here
    pass


def is_anagram_hashmap(s, t):
    """
    Hash Map Approach - O(n) time, O(n) space
    Count character frequencies and compare
    """
    if len(s) != len(t):
        return False

    # Build Hash Maps
    countS = {}
    countT = {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
    return True

    pass


def is_anagram_counter(s, t):
    """
    Counter Approach - O(n) time, O(n) space
    Use Counter from collections module
    """
    # Your solution here
    pass


def test_solution(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("listen", "silent", True),
        ("hello", "bello", False),
        ("", "", True),
        ("a", "ab", False),
        ("ab", "ba", True),
        ("aab", "baa", True),
        ("aabbcc", "abcabc", True),
        ("abcd", "dcba", True),
    ]

    for i, (s, t, expected) in enumerate(test_cases, 1):
        result = solution_func(s, t)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: '{s}' & '{t}' → {result} {status} (expected: {expected})")


if __name__ == "__main__":
    print("Valid Anagram Problem - Multiple Solutions")
    print("=" * 50)
    print(
        "\nProblem: Given two strings s and t, return true if t is an anagram of s, and false otherwise."
    )
    print("An anagram is a word formed by rearranging the letters of another word.")

    # Test sorting approach
    test_solution(is_anagram_sorting, "Sorting Approach O(n log n)")

    # Test hashmap approach
    test_solution(is_anagram_hashmap, "Hash Map Approach O(n)")

    # Test counter approach
    test_solution(is_anagram_counter, "Counter Approach O(n)")
