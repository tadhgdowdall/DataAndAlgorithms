from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    LeetCode 167: Two Sum II - Input Array Is Sorted

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
    order, find two numbers such that they add up to a specific target number.
    """
    pass


def twoSum_two_pointers(numbers: List[int], target: int) -> List[int]:
    """
    Two Pointers Approach (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    left = 0
    right = len(numbers) - 1

    while left < right:
        currentSum = numbers[left] + numbers[right]

        if currentSum < target:
            left += 1
        elif currentSum > target:
            right -= 1
        else:
            return [left + 1, right + 1]
    return []


def twoSum_binary_search(numbers: List[int], target: int) -> List[int]:
    """
    Binary Search Approach
    Time Complexity: O(n log n)
    Space Complexity: O(1)
    """
    pass


def twoSum_hashmap(numbers: List[int], target: int) -> List[int]:
    """
    HashMap Approach (like original Two Sum)
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    pass


def twoSum_brute_force(numbers: List[int], target: int) -> List[int]:
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)
    """
    pass


def test_solutions(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),
        ([-3, 3, 4, 90], 0, [1, 2]),
        ([0, 0, 3, 4], 0, [1, 2]),
        ([1, 2, 3, 4, 5, 6], 11, [5, 6]),
        ([5, 25, 75], 100, [2, 3]),
        ([1, 2], 3, [1, 2]),
    ]
    for i, (numbers_input, target, expected) in enumerate(test_cases, 1):
        try:
            result = solution_func(numbers_input, target)
            status = "✓" if result == expected else "✗"
            print(f"Test {i}: {result} (expected: {expected}) {status}")
        except Exception as e:
            print(f"Test {i}: Error - {e}")


if __name__ == "__main__":
    print("Two Sum II - Input Array Is Sorted - Multiple Solutions")
    print("=" * 65)

    test_solutions(twoSum_two_pointers, "Two Pointers O(n) - Optimal")
    test_solutions(twoSum_binary_search, "Binary Search O(n log n)")
    test_solutions(twoSum_hashmap, "HashMap O(n) - Extra Space")
    test_solutions(twoSum_brute_force, "Brute Force O(n²)")

    print(f"\n{'='*65}")
    print("Key Differences from Two Sum I:")
    print("✓ Array is sorted - enables two pointers approach")
    print("✓ Must use constant extra space - rules out hashmap")
    print("✓ Returns 1-indexed positions - add 1 to 0-based indices")
    print("✓ Guaranteed exactly one solution exists")
