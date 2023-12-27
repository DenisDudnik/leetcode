# https://leetcode.com/problems/3sum/

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    comb = [nums[i], nums[left], nums[right]]
                    res.append(comb)
                    while left < right and nums[left] == comb[1]:
                        left += 1
                    while left < right and nums[right] == comb[2]:
                        right -= 1
        return res


if __name__ == "__main__":
    # assert Solution().threeSum([-1,0,1,2,-1,-4]) == [[-1,-1,2],[-1,0,1]]
    assert Solution().threeSum([0, 1, 1]) == []
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]
