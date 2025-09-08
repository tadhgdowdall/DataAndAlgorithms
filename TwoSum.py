def two_sum(nums, target):
    """
    Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

    You may assume that each input would have exactly one solution, and you may not use the same element twice.
    You can return the answer in any order.

    Args:
        nums: List[int] - array of integers
        target: int - target sum

    Returns:
        List[int] - indices of the two numbers that add up to target

    Example:
        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
    """

    # First example is brute force

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def test_two_sum():
    """Test function with example inputs"""

    # Test case 1: Basic case
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = two_sum(nums1, target1)
    print(f"Test 1: nums={nums1}, target={target1}")
    print(f"Result: {result1}")
    print(f"Expected: [0, 1]")
    print()

    # Test case 2: Target at end
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = two_sum(nums2, target2)
    print(f"Test 2: nums={nums2}, target={target2}")
    print(f"Result: {result2}")
    print(f"Expected: [1, 2]")
    print()

    # Test case 3: Same number used twice
    nums3 = [3, 3]
    target3 = 6
    result3 = two_sum(nums3, target3)
    print(f"Test 3: nums={nums3}, target={target3}")
    print(f"Result: {result3}")
    print(f"Expected: [0, 1]")
    print()

    # Test case 4: Negative numbers
    nums4 = [-1, -2, -3, -4, -5]
    target4 = -8
    result4 = two_sum(nums4, target4)
    print(f"Test 4: nums={nums4}, target={target4}")
    print(f"Result: {result4}")
    print(f"Expected: [2, 4] (since -3 + -5 = -8)")
    print()

    # Test case 5: Larger array
    nums5 = [1, 5, 3, 7, 9, 2]
    target5 = 10
    result5 = two_sum(nums5, target5)
    print(f"Test 5: nums={nums5}, target={target5}")
    print(f"Result: {result5}")
    print(f"Expected: [0, 4] or [3, 5] (1+9=10 or 7+3=10)")
    print()


if __name__ == "__main__":
    print("Two Sum Problem")
    print("=" * 50)
    test_two_sum()
