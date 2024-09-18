from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ans = []
        start = None
        num = 0
        for num, interval in enumerate(intervals):
            if start is None:
                if newInterval[0] <= interval[1]:
                    if newInterval[0] > interval[0]:
                        start = interval[0]
                    if newInterval[0] <= interval[0]:
                        start = newInterval[0]
                elif newInterval[1] < interval[0]:
                    start = newInterval[0]
                else:
                    ans.append(interval)
            if start is not None:
                if interval[1] > newInterval[1] > interval[0]:
                    ans.append([start, interval[1]])
                    break
                elif newInterval[1] == interval[0]:
                    ans.append([start, interval[1]])
                    break
                elif newInterval[1] < interval[0]:
                    ans.append([start, newInterval[1]])
                    ans.append(interval)
                    break
        else:
            ans.append(newInterval) if start is None else ans.append([start, newInterval[1]])
        ans += intervals[num + 1:]
        return ans


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for interval in intervals:
            # the new interval is after the range of other interval, so we can leave the current interval baecause the new one does not overlap with it
            if interval[1] < newInterval[0]:
                result.append(interval)
            # the new interval's range is before the other, so we can add the new interval and update it to the current one
            elif interval[0] > newInterval[1]:
                result.append(newInterval)
                newInterval = interval
            # the new interval is in the range of the other interval, we have an overlap, so we must choose the min for start and max for end of interval
            elif interval[1] >= newInterval[0] or interval[0] <= newInterval[1]:
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(newInterval[1], interval[1])
        result.append(newInterval)
        return result
