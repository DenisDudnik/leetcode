# https://leetcode.com/problems/insert-interval/

from typing import List


# class Solution:
#     def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
#         left, right, center = [], [], newInterval
#         for idx, interval in enumerate(intervals):
#             if interval[-1] < newInterval[0]:
#                 left.append(interval)
#             elif interval[0] > newInterval[-1]:
#                 right = intervals[idx:]
#                 break
#             else:
#                 center[0] = min(center[0], interval[0])
#                 center[-1] = max(center[-1], interval[-1])
#         res = left + [center] + right
#         print(res)
#         return res


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        n = len(intervals)
        i = 0

        while i < n and intervals[i][-1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        while i < n and intervals[i][0] <= newInterval[-1]:
            newInterval[0] = min(intervals[i][0], newInterval[0])
            newInterval[1] = max(intervals[i][-1], newInterval[-1])
            i += 1
        result.append(newInterval)

        while i < n:
            result.append(intervals[i])
            i += 1

        return result


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
    assert Solution().insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8]) == [
        [1, 2],
        [3, 10],
        [12, 16],
    ]
