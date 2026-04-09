# https://leetcode.com/problems/sliding-window-maximum/

from typing import List

# 2026-04-09
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque

        res = []
        window = deque()
        for i, n in enumerate(nums):
            while window and nums[window[-1]] < n:
                window.pop()
            window.append(i)
            if window[0] <= i-k:
                window.popleft()
            if i + 1 >= k:
                res.append(nums[window[0]])
        return res


# tests
s = Solution()
assert s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert s.maxSlidingWindow([1], 1) == [1]
assert s.maxSlidingWindow([1, -1], 1) == [1, -1]
assert s.maxSlidingWindow([9, 11], 2) == [11]
assert s.maxSlidingWindow([4, -2], 2) == [4]
assert s.maxSlidingWindow([3, 1, 1, 3], 3) == [3, 3]
