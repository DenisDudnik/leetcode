# https://leetcode.com/problems/summary-ranges/

from typing import List


# 2025-12-25
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result = []
        ranges = []

        for n in nums:
            if not ranges or n - ranges[-1][1] > 1:
                ranges.append([n, n])
            else:
                ranges[-1][1] = n

        for range in ranges:
            result.append(f"{range[0]}->{range[1]}" if range[0] != range[1] else f"{range[0]}")

        return result


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
