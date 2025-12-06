# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


# 2025-12-06
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n

        nums_set = set(nums)
        longest = 0

        for num in nums_set:
            if num-1 not in nums_set:
                current = num + 1
                current_len = 1
                while current in nums_set:
                    current += 1
                    current_len += 1
                longest = max(longest, current_len)

        return longest


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
