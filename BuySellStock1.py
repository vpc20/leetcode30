# Best Time to Buy and Sell Stock
# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock),
# design an algorithm to find the maximum profit.
#
# Note that you cannot sell a stock before you buy one.
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.
#
# Example 2:
# Input: [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.

import sys


# def max_profit(prices):
#     profit = 0
#     for i in range(1, len(prices)):
#         for j in range(i):
#             if prices[i] - prices[j] > profit:
#                 profit = prices[i] - prices[j]
#     return profit


def max_profit(prices):
    if not prices:
        return 0
    min_price = sys.maxsize
    profit = -sys.maxsize
    for price in prices:
        min_price = min(min_price, price)
        profit = max(profit, price - min_price)
    return profit


# prices = [1, 2, 3, 4, 5]
# print(max_profit(prices))
# prices = [5, 4, 3, 2, 1]
# print(max_profit(prices))
# prices = [7, 1, 5, 3, 6, 4]
# print(max_profit(prices))
# prices = [1, 2]
# print(max_profit(prices))
# prices = [2, 4, 1]
# print(max_profit(prices))
# prices = [2, 10, 1, 5]
# print(max_profit(prices))
# prices = [1, 10, 2, 15]
# print(max_profit(prices))

prices = [7]
print(max_profit(prices))
prices = [7, 1]
print(max_profit(prices))
prices = [7, 1, 5]
print(max_profit(prices))
prices = [7, 1, 5, 3]
print(max_profit(prices))
prices = [7, 1, 5, 3, 6]
print(max_profit(prices))
prices = [7, 1, 5, 3, 6, 4]
print(max_profit(prices))
