# https://leetcode.com/problems/summary-ranges/

from typing import List


# 2025-12-23
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []

        result = []
        interval = [nums[0], nums[0]]

        for n in nums:
            if n - interval[1] > 1:
                result.append(f"{interval[0]}" if interval[0] == interval[1] else f"{interval[0]}->{interval[1]}")
                interval = [n, n]
            else:
                interval[1] = n

        result.append(f"{interval[0]}" if interval[0] == interval[1] else f"{interval[0]}->{interval[1]}")
        return result


if __name__ == "__main__":
    assert Solution().summaryRanges([0, 1, 2, 4, 5, 7]) == ["0->2", "4->5", "7"]
    assert Solution().summaryRanges([0, 2, 3, 4, 6, 8, 9]) == ["0", "2->4", "6", "8->9"]
    assert Solution().summaryRanges([]) == []
    assert Solution().summaryRanges([0]) == ["0"]
