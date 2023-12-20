# https://leetcode.com/problems/product-of-array-except-self/

from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post, res = 1, 1, [1]*len(nums)
        for i in range(len(nums)):
            j = -(i+1)
            res[i] *= pre
            res[j] *= post
            pre *= nums[i]
            post *= nums[j]
        return res


if __name__ == "__main__":
    assert Solution().productExceptSelf([1,2,3,4]) == [24,12,8,6]
    assert Solution().productExceptSelf([-1,1,0,-3,3]) == [0,0,9,0,0]
