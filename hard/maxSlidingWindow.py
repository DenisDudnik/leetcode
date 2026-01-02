# https://leetcode.com/problems/sliding-window-maximum/

from typing import List


# 2026-01-02
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        result = []
        d = deque()

        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()

            d.append(i)

            if d[0] <= i - k:
                d.popleft()

            if i >= k - 1:
                result.append(nums[d[0]])

        return result


# tests
s = Solution()
assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert s.maxSlidingWindow([1], 1) == [1]
assert s.maxSlidingWindow([1, -1], 1) == [1, -1]
assert s.maxSlidingWindow([9, 11], 2) == [11]
assert s.maxSlidingWindow([4, -2], 2) == [4]
