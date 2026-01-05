# https://leetcode.com/problems/summary-ranges/

from typing import List


# 2026-01-05
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        ranges = []

        for num in nums:
            if not ranges or ranges[-1][1] < num - 1:
                ranges.append([num, num])
            else:
                ranges[-1][1] = num

        for r in ranges:
            res.append(f"{r[0]}->{r[1]}" if r[0] != r[1] else f"{r[0]}")

        return res


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
