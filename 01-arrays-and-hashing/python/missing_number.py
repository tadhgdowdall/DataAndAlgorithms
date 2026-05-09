from typing import List


def missingNumber(nums: List[int]) -> int:
    """
    LeetCode 268: Missing Number

    Given an array nums containing n distinct numbers in the range [0, n],
    return the only number in the range that is missing from the array.
    """
    pass


def missingNumber_sum_formula(nums: List[int]) -> int:
    """
    Sum Formula Approach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Use mathematical sum formula: sum = n * (n + 1) / 2
    """
    pass


def missingNumber_xor(nums: List[int]) -> int:
    """
    XOR Bit Manipulation Approach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Use XOR properties: a ^ a = 0, a ^ 0 = a
    """
    pass


def missingNumber_set(nums: List[int]) -> int:
    """
    HashSet Approach
    Time Complexity: O(n)
    Space Complexity: O(n)

    Create set and check for missing number
    """
    number_set = set(nums)
    for i in range(len(nums) + 1):
        if i not in number_set:
            return i


def missingNumber_sorting(nums: List[int]) -> int:
    """
    Sorting Approach
    Time Complexity: O(n log n)
    Space Complexity: O(1)

    Sort array and find the gap
    """
    pass


def test_solutions(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([1], 0),
        ([0], 1),
        ([1, 2], 0),
        ([0, 1, 2, 3, 4, 5, 6, 7, 9], 8),
        ([1, 2, 3, 4, 5], 0),
        ([0, 1, 2, 3, 4], 5),
        ([2, 0], 1),
        ([4, 3, 2, 1], 0),
        ([0, 2, 3, 4, 5, 6, 7, 8, 9], 1),
    ]

    for i, (nums_input, expected) in enumerate(test_cases, 1):
        try:
            result = solution_func(nums_input)
            status = "✓" if result == expected else "✗"
            print(f"Test {i}: {result} (expected: {expected}) {status}")
            if result != expected:
                print(f"  Input: {nums_input}")
                print(f"  Range: [0, {len(nums_input)}]")

        except Exception as e:
            print(f"Test {i}: Error - {e}")


if __name__ == "__main__":
    print("Missing Number - Multiple Solutions")
    print("=" * 50)

    test_solutions(missingNumber_sum_formula, "Sum Formula O(n)")
    test_solutions(missingNumber_xor, "XOR Bit Manipulation O(n)")
    test_solutions(missingNumber_set, "HashSet O(n)")
    test_solutions(missingNumber_sorting, "Sorting O(n log n)")

    print(f"\n{'='*50}")
    print("Example Usage:")
    nums = [3, 0, 1]
    print(f"Array: {nums}")
    print(f"Range: [0, {len(nums)}] = [0, 1, 2, 3]")
    print("Explanation: Numbers 0, 1, 3 are present. Number 2 is missing.")
