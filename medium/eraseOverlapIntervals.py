# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


# 2025-12-24
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = -5 * 10**5
        removed = 0

        for interval in intervals:
            if interval[0] < last_end:
                removed += 1
            else:
                last_end = interval[1]

        return removed


# tests
s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
