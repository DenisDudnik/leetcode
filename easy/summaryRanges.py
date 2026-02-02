# https://leetcode.com/problems/summary-ranges/

from typing import List


# 2026-02-02
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result, ranges = [], []

        for n in nums:
            if ranges and ranges[-1][1] + 1 == n:
                ranges[-1][1] = n
            else:
                ranges.append([n, n])

        for r in ranges:
            result.append(f"{r[0]}" if r[0] == r[1] else f"{r[0]}->{r[1]}")

        return result


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
