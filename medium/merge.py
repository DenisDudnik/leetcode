# https://leetcode.com/problems/merge-intervals/

from typing import List


# 2025-12-22
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = []

        for interval in intervals:
            if result and interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)

        return result


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
