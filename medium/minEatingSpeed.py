# https://leetcode.com/problems/koko-eating-bananas/

from typing import List


# 2026-01-03
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2

            hours = 0
            for p in piles:
                hours += (p + mid - 1) // mid  # ceil(p / mid)

            if hours > h:
                left = mid + 1
            else:
                right = mid

        return left


# tests
s = Solution()
assert s.minEatingSpeed([3, 6, 7, 11], 8) == 4
assert s.minEatingSpeed([30, 11, 23, 4, 20], 5) == 30
assert s.minEatingSpeed([30, 11, 23, 4, 20], 6) == 23
