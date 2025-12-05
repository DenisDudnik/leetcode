# https://leetcode.com/problems/two-sum/

from typing import List


# 2025-12-05
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}

        for i in range(len(nums)):
            second = target - nums[i]
            if second in nums_dict:
                return [i, nums_dict[second]]
            nums_dict[nums[i]] = i

        return []


if __name__ == "__main__":
    assert sorted(Solution().twoSum(nums=[2, 7, 11, 15], target=9)) == sorted([0, 1])
    assert sorted(Solution().twoSum(nums=[3, 2, 4], target=6)) == sorted([1, 2])
    assert sorted(Solution().twoSum(nums=[3, 3], target=6)) == sorted([0, 1])
