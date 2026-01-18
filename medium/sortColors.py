# https://leetcode.com/problems/sort-colors/

from typing import List


# 2026-01-18
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        left, mid, right = 0, 0, len(nums) - 1

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[mid], nums[right] = nums[right], nums[mid]
                right -= 1


# tests
s = Solution()
a = [2, 0, 2, 1, 1, 0]
s.sortColors(a)
assert a == [0, 0, 1, 1, 2, 2]

a = [2, 0, 1]
s.sortColors(a)
assert a == [0, 1, 2]
