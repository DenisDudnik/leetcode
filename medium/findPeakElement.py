# https://leetcode.com/problems/find-peak-element/

from typing import List


# 2026-01-10
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


# tests
s = Solution()
assert s.findPeakElement([1, 2, 3, 1]) in [2]
assert s.findPeakElement([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
assert s.findPeakElement([1]) in [0]
assert s.findPeakElement([2, 1]) in [0]
assert s.findPeakElement([1, 2]) in [1]
