from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    """
    LeetCode 167: Two Sum II - Input Array Is Sorted

    Given a 1-indexed array of integers numbers that is already sorted in non-decreasing
    order, find two numbers such that they add up to a specific target number.

    Return the indices of the two numbers, index1 and index2, added by one as an integer
    array [index1, index2] of length 2.

    The tests are generated such that there is exactly one solution.
    You may not use the same element twice.
    Your solution must use only constant extra space.

    Example 1:
    Input: numbers = [2,7,11,15], target = 9
    Output: [1,2]
    Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Example 2:
    Input: numbers = [2,3,4], target = 6
    Output: [1,3]
    Explanation: The sum of 2 and 4 is 6. Therefore, index1 = 1, index2 = 3. We return [1, 3].

    Example 3:
    Input: numbers = [-1,0], target = -1
    Output: [1,2]
    Explanation: The sum of -1 and 0 is -1. Therefore, index1 = 1, index2 = 2. We return [1, 2].

    Constraints:
    - 2 <= numbers.length <= 3 * 10^4
    - -1000 <= numbers[i] <= 1000
    - numbers is sorted in non-decreasing order.
    - -1000 <= target <= 1000
    - The tests are generated such that there is exactly one solution.
    """
    # TODO: Implement your solution here
    pass


def twoSum_two_pointers(numbers: List[int], target: int) -> List[int]:
    """
    Two Pointers Approach (Optimal)
    Time Complexity: O(n)
    Space Complexity: O(1)

    Use left and right pointers, move based on sum comparison
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

    For each element, binary search for its complement
    """
    # TODO: Implement binary search solution
    pass


def twoSum_hashmap(numbers: List[int], target: int) -> List[int]:
    """
    HashMap Approach (like original Two Sum)
    Time Complexity: O(n)
    Space Complexity: O(n)

    Use hashmap to store seen numbers and their indices
    Note: This doesn't meet the constant space requirement
    """
    # TODO: Implement hashmap solution
    pass


def twoSum_brute_force(numbers: List[int], target: int) -> List[int]:
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)

    Check all possible pairs
    """
    # TODO: Implement brute force solution
    pass


def test_solutions(solution_func, solution_name):
    """Test a specific solution with all test cases"""
    print(f"\n{solution_name}")
    print("-" * 40)

    test_cases = [
        ([2, 7, 11, 15], 9, [1, 2]),  # Standard case
        ([2, 3, 4], 6, [1, 3]),  # Skip middle element
        ([-1, 0], -1, [1, 2]),  # Negative numbers
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),  # Duplicates
        ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),  # Multiple valid pairs (first one)
        ([-3, 3, 4, 90], 0, [1, 2]),  # Zero sum
        ([0, 0, 3, 4], 0, [1, 2]),  # Both zeros
        ([1, 2, 3, 4, 5, 6], 11, [5, 6]),  # Last two elements
        ([5, 25, 75], 100, [2, 3]),  # Large numbers
        ([1, 2], 3, [1, 2]),  # Minimum length
    ]
    for i, (numbers_input, target, expected) in enumerate(test_cases, 1):
        try:
            result = solution_func(numbers_input, target)
            status = "✓" if result == expected else "✗"

            # Verify the result is correct by checking the actual sum
            if len(result) == 2:
                idx1, idx2 = result
                if 1 <= idx1 < idx2 <= len(numbers_input):
                    actual_sum = numbers_input[idx1 - 1] + numbers_input[idx2 - 1]
                    sum_correct = actual_sum == target
                    if not sum_correct:
                        status = "✗ (sum mismatch)"
                else:
                    status = "✗ (invalid indices)"
            else:
                status = "✗ (invalid format)"

            print(f"Test {i}: {result} (expected: {expected}) {status}")

            if result != expected and status.startswith("✓"):
                # Different indices but potentially valid answer
                idx1, idx2 = result
                sum_val = numbers_input[idx1 - 1] + numbers_input[idx2 - 1]
                print(
                    f"  Note: Different valid answer - nums[{idx1-1}] + nums[{idx2-1}] = {numbers_input[idx1-1]} + {numbers_input[idx2-1]} = {sum_val}"
                )

        except Exception as e:
            print(f"Test {i}: Error - {e}")


if __name__ == "__main__":
    print("Two Sum II - Input Array Is Sorted - Multiple Solutions")
    print("=" * 65)

    # Test two pointers (optimal)
    test_solutions(twoSum_two_pointers, "Two Pointers O(n) - Optimal")

    # Test binary search
    test_solutions(twoSum_binary_search, "Binary Search O(n log n)")

    # Test hashmap
    test_solutions(twoSum_hashmap, "HashMap O(n) - Extra Space")

    # Test brute force
    test_solutions(twoSum_brute_force, "Brute Force O(n²)")

    # Test main solution (when implemented)
    # test_solutions(twoSum, "Main Solution")

    print(f"\n{'='*65}")
    print("Example Usage:")
    numbers = [2, 7, 11, 15]
    target = 9
    print(f"Array: {numbers} (1-indexed)")
    print(f"Target: {target}")
    # result = twoSum_two_pointers(numbers, target)
    # print(f"Result: {result}")
    # print(f"Explanation: numbers[{result[0]-1}] + numbers[{result[1]-1}] = {numbers[result[0]-1]} + {numbers[result[1]-1]} = {target}")
    print("Remember: Returns 1-indexed positions, not 0-indexed!")

    print(f"\n{'='*65}")
    print("Key Differences from Two Sum I:")
    print("✓ Array is sorted - enables two pointers approach")
    print("✓ Must use constant extra space - rules out hashmap")
    print("✓ Returns 1-indexed positions - add 1 to 0-based indices")
    print("✓ Guaranteed exactly one solution exists")
