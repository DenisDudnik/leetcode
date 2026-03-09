# https://leetcode.com/problems/summary-ranges/

from typing import List


# 2026-03-09
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        intervals = []
        for n in nums:
            if intervals and n - 1 <= intervals[-1][1]:
                intervals[-1][1] = n
            else:
                intervals.append([n, n])

        res = [
            f"{interval[0]}" if interval[0] == interval[1] else f"{interval[0]}->{interval[1]}"
            for interval in intervals
        ]

        return res


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
