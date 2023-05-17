# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k, i = len(nums), 0
        while True:
            if i >= len(nums) - 1:
                return k
            if nums[i] == nums[i+1]:
                nums.pop(i+1)
                k -= 1
                continue
            i += 1


if __name__ == "__main__":
    nums = [1,1,2] # Input array
    expectedNums = [1,2] # The expected answer with correct length

    k = Solution().removeDuplicates(nums) # Calls your implementation
    print(nums)

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]


    nums = [0,0,1,1,1,2,2,3,3,4] # Input array
    expectedNums = [0,1,2,3,4] # The expected answer with correct length

    k = Solution().removeDuplicates(nums) # Calls your implementation
    print(nums)

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]
