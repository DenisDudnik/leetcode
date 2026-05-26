# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


# 2026-05-26
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        res = 0
        end = -6 * 10**4
        for interval in intervals:
            if interval[0] < end:
                res += 1
            else:
                end = interval[1]
        return res


# tests
s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
assert s.eraseOverlapIntervals([[1, 100], [11, 22], [1, 11], [2, 12]]) == 2
