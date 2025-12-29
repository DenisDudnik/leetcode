# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


# 2025-12-28
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        last_end = -5 * 10**5
        removed = 0

        for interval in intervals:
            if interval[0] >= last_end:
                last_end = interval[1]
            else:
                removed += 1

        return removed


# tests
s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
