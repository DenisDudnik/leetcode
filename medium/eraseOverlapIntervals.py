# https://leetcode.com/problems/non-overlapping-intervals/

from typing import List


# 2026-01-04
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        result = 0
        intervals.sort(key=lambda x: x[1])
        last_end = -5 * 10**5

        for interval in intervals:
            if interval[0] >= last_end:
                last_end = interval[1]
            else:
                result += 1

        return result


# tests
s = Solution()
assert s.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert s.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]) == 2
assert s.eraseOverlapIntervals([[1, 2], [2, 3]]) == 0
assert s.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2
