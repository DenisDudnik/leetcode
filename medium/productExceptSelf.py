# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# 2025-12-16
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        pre = 1
        for i in range(len(nums)):
            result[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= post
            post *= nums[i]

        return result


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
