from typing import List


class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        lowest = nums[0]
        max_profit = -1
        for i in range(len(nums)):
            if nums[i] < lowest:
                lowest = nums[i]
            max_profit = max(nums[i] - lowest, max_profit)
        return max_profit
