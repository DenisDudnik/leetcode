# https://leetcode.com/problems/merge-intervals/

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for interval in intervals[1:]:
            if interval[0] <= res[-1][-1]:
                if interval[1] > res[-1][-1]:
                    res[-1][-1] = interval[1]
            else:
                res.append(interval)
        print(res)
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
