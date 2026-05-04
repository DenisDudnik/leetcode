# https://leetcode.com/problems/two-sum/

from typing import List


# 2026-05-04
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        for i, n in enumerate(nums):
            second = target - n
            if second in indices:
                return [indices[second], i]
            indices[n] = i
        return []


if __name__ == "__main__":
    assert sorted(Solution().twoSum(nums=[2, 7, 11, 15], target=9)) == sorted([0, 1])
    assert sorted(Solution().twoSum(nums=[3, 2, 4], target=6)) == sorted([1, 2])
    assert sorted(Solution().twoSum(nums=[3, 3], target=6)) == sorted([0, 1])
