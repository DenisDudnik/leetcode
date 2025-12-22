# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# 2025-12-22
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = current = 0

        for n in nums_set:
            if n - 1 not in nums_set:
                cur = n
                while cur in nums_set:
                    current += 1
                    cur += 1
                longest = max(current, longest)
                current = 0

        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
