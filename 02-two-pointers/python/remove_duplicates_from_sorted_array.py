from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    LeetCode 26: Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the duplicates
    in-place such that each unique element appears only once.
    """
    pass


def removeDuplicates_brute_force(nums: List[int]) -> int:
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    pass


def removeDuplicates_two_pointers(nums: List[int]) -> int:
    """
    Two Pointers Approach
    Time Complexity: O(n)
    Space Complexity: O(1)

    Use slow and fast pointers to keep unique elements
    """
    if not nums:
        return 0

    j = 0
    for i in range(1, len(nums)):
        if nums[j] != nums[i]:
            j += 1
            nums[j] = nums[i]
    return j + 1


def test_solutions(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([1, 1, 2], 2, [1, 2]),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], 5, [0, 1, 2, 3, 4]),
        ([1, 1, 1], 1, [1]),
        ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
        ([1], 1, [1]),
        ([1, 1], 1, [1]),
        ([-3, -1, 0, 0, 0, 3, 3], 4, [-3, -1, 0, 3]),
        ([1, 1, 1, 1, 1, 1, 1], 1, [1]),
    ]

    for i, (nums_input, expected_length, expected_unique) in enumerate(test_cases, 1):
        try:
            nums = nums_input.copy()
            result_length = solution_func(nums)
            length_correct = result_length == expected_length
            unique_correct = nums[:result_length] == expected_unique
            overall_status = "✓" if (length_correct and unique_correct) else "✗"

            print(f"Test {i}:")
            print(f"  Input: {nums_input}")
            print(f"  Length: {result_length} (expected: {expected_length}) {'✓' if length_correct else '✗'}")
            print(f"  Unique: {nums[:result_length]} (expected: {expected_unique}) {'✓' if unique_correct else '✗'}")
            print(f"  Overall: {overall_status}")

        except Exception as e:
            print(f"Test {i}: Error - {e}")
        print()


if __name__ == "__main__":
    print("Remove Duplicates from Sorted Array - Multiple Solutions")
    print("=" * 65)

    test_solutions(removeDuplicates_brute_force, "Brute Force O(n²)")
    test_solutions(removeDuplicates_two_pointers, "Two Pointers O(n)")

    print(f"\n{'='*65}")
    print("Example Usage:")
    nums = [1, 1, 2, 2, 3, 3, 4]
    print(f"Original: {nums}")
    print("Explanation: Keep only the first occurrence of each unique element")
