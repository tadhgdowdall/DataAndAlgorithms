package main

// LeetCode 121: Best Time to Buy and Sell Stock
//
// You are given an array prices where prices[i] is the price of a given stock on day i.
// You want to maximize your profit by choosing a single day to buy one stock and choosing
// a different day in the future to sell that stock.
//
// Return the maximum profit you can achieve from this transaction.
// If you cannot achieve any profit, return 0.

func maxProfits(prices []int) int {
	// 2 pointers problem

	left := 0
	right := 1
	maxProfit := 0

	for right < len(prices) {
		if prices[left] < prices[right] {
			profit := prices[right] - prices[left]
			if profit > maxProfit {
				maxProfit = profit
			}
			right++
		} else {
			left = right
			right++
		}
	}
	return maxProfit
}
