# 1. Write your solutions here


def concat_array_method1(nums):
    """Simple approach - concatenate with +"""
    return nums + nums


def concat_array_method2(nums):
    """Pythonic approach - multiply list by 2"""
    n = len(nums) - 1

    ans = [0] * (2 * n)

    for i in range(n):
        ans[i] = nums[i]
        ans[i + n] = nums[i]
    return ans


# 2. Test harness (already set up)


def test_solution(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([1, 2, 1], [1, 2, 1, 1, 2, 1]),
        ([1, 3, 2, 1], [1, 3, 2, 1, 1, 3, 2, 1]),
        ([5], [5, 5]),
        ([0, 0, 0], [0, 0, 0, 0, 0, 0]),
        ([], []),  # edge case: empty array
    ]

    for i, (nums, expected) in enumerate(test_cases, 1):
        result = solution_func(nums)
        print(f"Test {i}: {result} (expected: {expected})")


# 3. Run tests here


if __name__ == "__main__":
    print("Concatenation of Array Problem - Multiple Solutions")
    print("=" * 50)

    test_solution(concat_array_method1, "Method 1")
    test_solution(concat_array_method2, "Method 2")
