from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for k, v in enumerate(nums):
            first = target - v
            if first in nums_dict.keys():
                return [k, nums_dict[first]]
            nums_dict[v] = k
