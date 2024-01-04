# https://leetcode.com/problems/contains-duplicate-ii/

from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        cache = {}
        for i, num in enumerate(nums):
            if num in cache and i - cache[num] <= k:
                return True
            cache[num] = i
        return False


if __name__ == "__main__":
    assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3) == True
    assert Solution().containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1) == True
    assert Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2) == False
