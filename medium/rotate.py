# https://leetcode.com/problems/rotate-array/

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # k = k % len(nums)
        # nums.reverse()
        # nums_len = len(nums)

        # for idx in range(k//2):
        #     nums[k-idx-1], nums[idx] = nums[idx], nums[k-idx-1]
        # for idx in range(-1, -((nums_len - k)//2+1), -1):
        #     nums[-(nums_len-k+idx+1)], nums[idx] = nums[idx], nums[-(nums_len-k+idx+1)]

        k=k%len(nums)
        nums.reverse()
    
        # Reverse the first k elements
        nums[:k] = reversed(nums[:k])
    
        # Reverse the remaining elements
        nums[k:] = reversed(nums[k:])

        print(nums)


if __name__ == "__main__":
    nums, k = [1,2,3,4,5,6,7], 4
    Solution().rotate(nums = nums, k = k)
    assert nums == [4,5,6,7,1,2,3]
    
    nums, k = [-1,-100,3,99], 2
    Solution().rotate(nums = nums, k = k)
    assert nums == [3,99,-1,-100]
    
    nums, k = [1,2], 3
    Solution().rotate(nums = nums, k = k)
    assert nums == [2,1]
