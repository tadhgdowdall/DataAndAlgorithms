from typing import List


def removeDuplicates(nums: List[int]) -> int:
    """
    LeetCode 26: Remove Duplicates from Sorted Array

    Given an integer array nums sorted in non-decreasing order, remove the duplicates
    in-place such that each unique element appears only once. The relative order of
    the elements should be kept the same.

    Since it is impossible to change the length of the array in some languages, you
    must instead have the result be placed in the first part of the array nums.
    More formally, if there are k elements after removing the duplicates, then the
    first k elements of nums should hold the final result.

    Return k (the number of unique elements).

    Example 1:
    Input: nums = [1,1,2]
    Output: 2, nums = [1,2,_]
    Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
    It does not matter what you leave beyond the returned k (hence they are underscores).

    Example 2:
    Input: nums = [0,0,1,1,1,2,2,3,3,4]
    Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

    Constraints:
    - 1 <= nums.length <= 3 * 10^4
    - -100 <= nums[i] <= 100
    - nums is sorted in non-decreasing order.
    """
    # TODO: Implement your solution here
    pass


def removeDuplicates_brute_force(nums: List[int]) -> int:
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)

    Remove duplicates by shifting elements
    """
    # TODO: Implement brute force solution
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
            # Create a copy since the function modifies the array in-place
            nums = nums_input.copy()
            result_length = solution_func(nums)

            # Check if length is correct
            length_correct = result_length == expected_length

            # Check if the first k elements match expected unique elements
            unique_correct = nums[:result_length] == expected_unique

            overall_status = "✓" if (length_correct and unique_correct) else "✗"

            print(f"Test {i}:")
            print(f"  Input: {nums_input}")
            print(
                f"  Length: {result_length} (expected: {expected_length}) {'✓' if length_correct else '✗'}"
            )
            print(
                f"  Unique: {nums[:result_length]} (expected: {expected_unique}) {'✓' if unique_correct else '✗'}"
            )
            print(f"  Overall: {overall_status}")

        except Exception as e:
            print(f"Test {i}: Error - {e}")
        print()


if __name__ == "__main__":
    print("Remove Duplicates from Sorted Array - Multiple Solutions")
    print("=" * 65)

    # Test brute force
    test_solutions(removeDuplicates_brute_force, "Brute Force O(n²)")

    # Test two pointers
    test_solutions(removeDuplicates_two_pointers, "Two Pointers O(n)")

    # Test main solution (when implemented)
    # test_solutions(removeDuplicates, "Main Solution")

    print(f"\n{'='*65}")
    print("Example Usage:")
    nums = [1, 1, 2, 2, 3, 3, 4]
    print(f"Original: {nums}")
    # length = removeDuplicates_two_pointers(nums)
    # print(f"After removal: {nums[:length]} (length: {length})")
    print("Explanation: Keep only the first occurrence of each unique element")
