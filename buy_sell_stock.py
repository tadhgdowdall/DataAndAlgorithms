def max_profit(prices):
    """
    LeetCode 121: Best Time to Buy and Sell Stock

    You are given an array prices where prices[i] is the price of a given stock on day i.
    You want to maximize your profit by choosing a single day to buy one stock and choosing
    a different day in the future to sell that stock.

    Return the maximum profit you can achieve from this transaction.
    If you cannot achieve any profit, return 0.

    Example 1:
    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

    Example 2:
    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.

    Constraints:
    - 1 <= prices.length <= 10^5
    - 0 <= prices[i] <= 10^4
    """
    # TODO: Implement your solution here
    pass


def max_profit_brute_force(prices):
    """
    Brute Force Approach
    Time Complexity: O(n²)
    Space Complexity: O(1)

    Check all possible buy-sell combinations
    """
    # TODO: Implement brute force solution
    pass


def max_profit_optimal(prices):
    """
    Optimal Approach - One Pass
    Time Complexity: O(n)
    Space Complexity: O(1)

    Keep track of minimum price seen so far and maximum profit
    """
    left, right = 0, 1
    maxProfit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            maxProfit = max(maxProfit, profit)
        else:
            left = right
        right += 1

    return maxProfit


def max_profit_kadane_like(prices):
    """
    Kadane's Algorithm Variation
    Time Complexity: O(n)
    Space Complexity: O(1)

    Transform to maximum subarray problem
    """
    # TODO: Implement using Kadane's algorithm approach
    pass


# Test cases
def test_solutions():
    """Test all implementations"""
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),  # Buy at 1, sell at 6
        ([7, 6, 4, 3, 1], 0),  # No profit possible
        ([1, 2, 3, 4, 5], 4),  # Buy at 1, sell at 5
        ([5, 4, 3, 2, 1], 0),  # Decreasing prices
        ([1, 2], 1),  # Simple case
        ([2, 1], 0),  # No profit
        ([1], 0),  # Single price
        ([3, 3, 5, 0, 0, 3, 1, 4], 4),  # Buy at 0, sell at 4
    ]

    solutions = [
        ("Brute Force", max_profit_brute_force),
        ("Optimal", max_profit_optimal),
        ("Kadane-like", max_profit_kadane_like),
        ("Main Solution", max_profit),
    ]

    for prices, expected in test_cases:
        print(f"Input: {prices}")
        print(f"Expected: {expected}")

        for name, func in solutions:
            try:
                result = func(prices)
                status = "✓" if result == expected else "✗"
                print(f"  {name}: {result} {status}")
            except Exception as e:
                print(f"  {name}: Error - {e}")
        print()


if __name__ == "__main__":
    print("Best Time to Buy and Sell Stock - Multiple Solutions")
    print("=" * 60)

    # Test brute force

    # Test optimal (your solution)

    # Test Kadane-like

    # Test main solution (when implemented)
    # test_solutions(max_profit, "Main Solution")

    print(f"\n{'='*60}")
    print("Example Usage:")
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Prices: {prices}")
    print(f"Max Profit (Your Solution): {max_profit_optimal(prices)}")
    print("Explanation: Buy at price 1 (day 1), sell at price 6 (day 4) = profit of 5")
