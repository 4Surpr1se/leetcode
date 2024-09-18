from typing import List


class Solution:
    # AHAHHAHAAAAAAAAAAAAAHAHAAAHAHHAAAAAAAAAAAAAAAAAHHAHAHHAHAHAHAHAHHAHAHAHHA HA!

    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        range_start = range_end = int(nums[0])
        return_list = []
        for i in range(len(nums) - 1):
            if range_end > int(nums[i]):
                continue
            elif isinstance(nums[i + 1], str) and isinstance(nums[i], str):
                if int(nums[i + 1]) == int(nums[i]):
                    continue
                else:
                    return_list.append([range_start, range_end])
                    range_start = range_end = int(nums[i + 1])
            elif isinstance(nums[i + 1], str) and int(nums[i + 1]) == nums[i] + 1:
                range_end += 1
            elif isinstance(nums[i + 1], str) and int(nums[i + 1]) == nums[i]:
                range_end += 1
            elif isinstance(nums[i + 1], str) and int(nums[i + 1]) != nums[i] + 1:
                return_list.append([range_start, range_end])
                range_start = range_end = int(nums[i + 1])
            elif isinstance(nums[i], str) and nums[i + 1] != int(nums[i]):
                return_list.append([range_start, range_end])
                range_start = range_end = int(nums[i + 1])
            elif isinstance(nums[i], str) and nums[i + 1] == int(nums[i]):
                continue

            elif nums[i + 1] == nums[i] + 1:
                range_end += 1
            elif nums[i + 1] != nums[i]:
                return_list.append([range_start, range_end])
                range_start = range_end = int(nums[i + 1])
        return_list.append([range_start, range_end])

        return return_list

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        initial = []
        for interval in intervals:
            if interval[0] == interval[1]:
                initial.append('0' + str(interval[0]))
            else:
                for val in range(interval[0], interval[1]):
                    initial.append(val)

                initial.append('0' + str(val + 1))
        self.merge_sort(initial, 0, len(initial) - 1)
        return self.summaryRanges(initial)

    def merge_merge(self, arr, left, mid, right):
        # todo переделать этот шлак
        n1 = mid - left + 1
        n2 = right - mid

        L = [0] * n1
        R = [0] * n2

        for i in range(n1):
            L[i] = arr[left + i]
        for j in range(n2):
            R[j] = arr[mid + 1 + j]

        i = 0
        j = 0
        k = left

        while i < n1 and j < n2:
            if int(L[i]) <= int(R[j]):
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L[],
        # if there are any
        while i < n1:
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R[],
        # if there are any
        while j < n2:
            arr[k] = R[j]
            j += 1
            k += 1

    def merge_sort(self, arr, left, right):
        if left < right:
            mid = (left + right) // 2

            self.merge_sort(arr, left, mid)
            self.merge_sort(arr, mid + 1, right)
            self.merge_merge(arr, left, mid, right)


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        ans = []

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans


print(sorted([[1, 6], [1, 4]], key=lambda x: x[0]))
