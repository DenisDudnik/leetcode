# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        arrows, left, right = 1, *points[0]
        for point in points:
            if point[0] <= right:
                left = max(left, point[0])
                right = min(right, point[1])
            else:
                arrows += 1
                left, right = point[0], point[1]
        print(arrows)
        return arrows


if __name__ == "__main__":
    assert Solution().findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]) == 2
    assert Solution().findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]) == 4
    assert Solution().findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]) == 2
