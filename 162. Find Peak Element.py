from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        high = len_ = len(nums)
        low = 0

        while True:
            mid = low + (high - low) // 2
            mid_val = nums[mid]
            before, after = mid - 1, mid + 1
            before_val = nums[before] if before >= 0 else float('-inf')
            after_val = nums[after] if after < len_ else float('-inf')
            if mid_val > before_val and mid_val > after_val:
                return mid
            elif before_val < mid_val < after_val:
                low = mid + 1
            elif before_val > mid_val > after_val:
                high = mid - 1
            else:
                high = mid - 1


print(Solution().findPeakElement(list(reversed([1, 2, 3, 5, 4]))))
print(Solution().findPeakElement([2, 3, 4, 3, 2, 1]))
