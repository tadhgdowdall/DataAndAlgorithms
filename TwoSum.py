def two_sum_brute_force(nums, target):
    """Brute Force Approach - O(n^2) time, O(1) space"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []


def two_sum_hashmap(nums, target):
    """Hash Map Approach - O(n) time, O(n) space"""
    seen = {}
    for index, num in enumerate(nums):
        difference = target - num
        if difference in seen:
            return [seen[difference], index]
        seen[num] = index
    return []


def test_solution(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 5, 3, 7, 9, 2], 10, "multiple solutions"),
    ]

    for i, (nums, target, expected) in enumerate(test_cases, 1):
        result = solution_func(nums, target)
        print(f"Test {i}: {result} (expected: {expected})")


if __name__ == "__main__":
    print("Two Sum Problem - Multiple Solutions")
    print("=" * 50)

    # Test brute force
    test_solution(two_sum_brute_force, "Brute Force O(n²)")

    # Test hashmap
    test_solution(two_sum_hashmap, "Hash Map O(n)")
