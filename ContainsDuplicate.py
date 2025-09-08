def contains_duplicate_brute_force(nums):
    """
    Brute Force Approach - O(n^2) time, O(1) space
    Check every pair of elements
    """
    # Your solution here
    pass


def contains_duplicate_sorting(nums):
    """
    Sorting Approach - O(n log n) time, O(1) space
    Sort array and check adjacent elements
    """
    nums.sort()

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            return True
    return False


def contains_duplicate_hashset(nums):
    """
    Hash Set Approach - O(n) time, O(n) space
    Use set to track seen elements
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


def test_solution(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([], False),
        ([1], False),
        ([1, 2], False),
        ([2, 2], True),
        ([1, 5, 9, 1, 5, 9], True),
        ([-1, -2, -3], False),
        ([0, 0], True),
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution_func(nums)
        status = "✓" if result == expected else "✗"
        print(f"Test {i}: {nums} → {result} {status} (expected: {expected})")


if __name__ == "__main__":
    print("Contains Duplicate Problem - Multiple Solutions")
    print("=" * 50)
    print("\nProblem: Given an integer array nums, return true if any value appears")
    print("at least twice in the array, and return false if every element is distinct.")

    # Test brute force
    test_solution(contains_duplicate_brute_force, "Brute Force O(n²)")

    # Test sorting
    test_solution(contains_duplicate_sorting, "Sorting O(n log n)")

    # Test hashset
    test_solution(contains_duplicate_hashset, "Hash Set O(n)")
