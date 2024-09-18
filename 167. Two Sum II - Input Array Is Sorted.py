from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        tmp = 0
        storage = {}
        while True:
            tmp_val = numbers[tmp]
            if val := storage.get(target - tmp_val):
                if tmp != val:
                    return [tmp + 1, val + 1]
            low = 0
            high = len(numbers) - 1
            while low <= high:
                x = target - tmp_val
                mid = low + (high - low) // 2
                if numbers[mid] == x and mid != tmp:
                    return [tmp + 1, mid + 1]
                elif numbers[mid] < x:
                    low = mid + 1
                else:
                    high = mid - 1
                storage[numbers[mid]] = mid
            tmp += 1


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = self.get_high_binary(numbers, target) or len(numbers) - 1
        while True:
            sum_ = numbers[low] + numbers[high]
            if target == sum_:
                return [low + 1, high + 1]
            if target > sum_:
                low += 1
            if target < sum_:
                high -= 1

    def get_high_binary(self, numbers, target):
        """Можно доделать, чтобы они отдавал не len(n) - 1,
         а ближайшее справа или равное target'у значение, но мне чет впадлу"""



print(Solution().twoSum([2, 7, 11, 15], 9))
