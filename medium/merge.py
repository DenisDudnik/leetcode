# https://leetcode.com/problems/merge-intervals/

from typing import List


# 2026-01-18
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        intervals.sort(key=lambda x: x[0])

        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                res[-1][1] = max(res[-1][1], interval[1])
            else:
                res.append(interval)
        return res


if __name__ == "__main__":
    assert Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]]) == [
        [1, 6],
        [8, 10],
        [15, 18],
    ]
    assert Solution().merge([[1, 4], [4, 5]]) == [[1, 5]]
    assert Solution().merge([[1, 6], [4, 5]]) == [[1, 6]]
    assert Solution().merge([[1, 4]]) == [[1, 4]]
    assert Solution().merge([[1, 4], [0, 4]]) == [[0, 4]]
    assert Solution().merge([[0, 1], [3, 5], [4, 5], [1, 6]]) == [[0, 6]]
