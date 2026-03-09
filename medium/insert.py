# https://leetcode.com/problems/insert-interval/

from typing import List


# 2026-03-09
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1

        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res


if __name__ == "__main__":
    assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5]) == [
        [1, 5],
        [6, 9],
    ]
    assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[4, 5]) == [
        [1, 3],
        [4, 5],
        [6, 9],
    ]
    assert Solution().insert(intervals=[[1, 3], [6, 9]], newInterval=[14, 15]) == [
        [1, 3],
        [6, 9],
        [14, 15],
    ]
    assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
