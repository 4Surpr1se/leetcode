from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        amount_sum = 0
        lowest_now = prices[0]
        for i in range(1, len(prices)):
            if prices[i] > lowest_now:
                amount_sum += prices[i] - lowest_now
                lowest_now = prices[i]
            if prices[i] < lowest_now:
                lowest_now = prices[i]
        return amount_sum


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        if len(prices) == 1:
            return 0

        for i in range(len(prices) - 1):
            if prices[i] < prices[i + 1]:
                profit = profit + (prices[i + 1] - prices[i])
        return profit
