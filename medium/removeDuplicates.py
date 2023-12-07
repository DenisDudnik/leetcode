# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        num_count = 1
        idx = 1
        while True:
            try:
                if nums[idx] == nums[idx-1]:
                    if num_count < 2:
                        num_count += 1
                        idx += 1
                    else:
                        nums.pop(idx)
                else:
                    num_count = 1
                    idx += 1
            except IndexError:
                return len(nums)
            
        


if __name__ == "__main__":
    nums = [1,1,1,2,2,3] # Input array
    expectedNums = [1,1,2,2,3] # The expected answer with correct length

    print(nums)
    k = Solution().removeDuplicates(nums) # Calls your implementation

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]

    print("--------")
    nums = [0,0,1,1,1,1,2,3,3] # Input array
    expectedNums = [0,0,1,1,2,3,3] # The expected answer with correct length

    print(nums)
    k = Solution().removeDuplicates(nums) # Calls your implementation

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]