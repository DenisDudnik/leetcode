# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# 2026-03-09
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            i = 1
            while num + i in nums_set:
                i += 1
            longest = max(longest, i)
        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
