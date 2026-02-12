# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


# 2026-02-11
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            k = (left + right) // 2
            hours = sum((p + k - 1) // k for p in piles)
            if hours <= h:
                right = k
            else:
                left = k + 1

        return left


# tests
s = Solution()
assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
