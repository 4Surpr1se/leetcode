from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        points.sort(key=lambda x: x[0])
        start_end = points[0]
        counter = 1
        for point in points:
            if start_end[1] >= point[0]:
                start_end[0] = point[0]
                start_end[1] = min(start_end[1], point[1])
            else:
                start_end = point
                counter += 1
        return counter


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        end = points[0][1]

        for balloon in points:
            start, end_of_balloon = balloon
            if start > end:
                arrows += 1
                end = end_of_balloon
        return arrows
