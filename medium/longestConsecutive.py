# https://leetcode.com/problems/longest-consecutive-sequence/

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        max_len = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 in nums_set:
                continue
            i = 1
            while num + i in nums_set:
                i += 1
            max_len = max(max_len, i)

        return max_len


if __name__ == "__main__":
    assert Solution().longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
    assert Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]) == 9
