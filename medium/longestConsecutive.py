# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# 2026-02-05
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        nums_set = set(nums)

        for n in nums_set:
            i = 1
            if n - 1 not in nums_set:
                while n + i in nums_set:
                    i += 1
            longest = max(longest, i)
        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
