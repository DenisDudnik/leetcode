# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

# 2026-03-16
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        pre = 1
        for i in range(n):
            res[i] = pre
            pre *= nums[i]

        post = 1
        for i in range(n - 1, -1, -1):
            res[i] *= post
            post *= nums[i]
        return res


if __name__ == "__main__":
    assert Solution().productExceptSelf([1, 2, 3, 4]) == [24, 12, 8, 6]
    assert Solution().productExceptSelf([-1, 1, 0, -3, 3]) == [0, 0, 9, 0, 0]
