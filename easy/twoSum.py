# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for k, v in enumerate(nums):
            first = target - v
            if first in nums_dict:
                return [k, nums_dict[first]]
            nums_dict[v] = k


if __name__ == "__main__":
    assert sorted(Solution().twoSum(nums=[2, 7, 11, 15], target=9)) == sorted([0, 1])
    assert sorted(Solution().twoSum(nums=[3, 2, 4], target=6)) == sorted([1, 2])
    assert sorted(Solution().twoSum(nums=[3, 3], target=6)) == sorted([0, 1])
