def memoized(func):
    cache = dict()

    def inner(n):
        if n not in cache:
            cache[n] = func(n)
            print(cache[n])
            return cache[n]

    return inner


@memoized
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)


def fibonacci_memoized(num, cache={}):
    if num in cache:
        print(cache[num])
        return cache[num]
    else:
        if num <= 1:
            cache[num] = num
            return num
        else:
            cache[num] = fibonacci_memoized(num - 1) + fibonacci_memoized(num - 2)
            return cache[num]


# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them
#  is that adjacent houses have security system connected
# and it will automatically contact the police if two adjacent houses were broken into on the same night.
# Given a list of non-negative integers representing the amount of money of each house,
# determine the maximum amount of money you can rob tonight without alerting the police.

def rob(nums):
    sum_1 = sum_2 = 0
    for i in range(len(nums)):
        if i % 2 == 0:
            sum_1 = max(sum_1 + nums[i], sum_2)
        else:
            sum_2 = max(sum_2 + nums[i], sum_1)
    return max(sum_1, sum_2)


# Say you have an array for which the ith element is the price of a given stock on day i.
# If you were only permitted to complete at most one transaction
# (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
# Note that you cannot sell a stock before you buy one.
# Example 1:
# Input: [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
#              Not 7-1 = 6, as selling price needs to be larger than buying price.

def max_profit(prices):
    if not prices:
        return 0
    b_price = prices[0]
    profit = 0
    for p in prices:
        b_price = min(p, b_price)
        temp_profit = p - b_price
        profit = max(profit, temp_profit)
    return profit


# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps.
# In how many distinct ways can you climb to the top?
# Example 1:
# Input: 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

# Example 2:
# Input: 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

def climb_stairs(n) -> int:
    rt = (1, 1)
    for i in range(n - 1):
        rt = (rt[1], rt[0] + rt[1])
    return rt[1]
