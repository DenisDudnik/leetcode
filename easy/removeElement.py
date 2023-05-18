# https://leetcode.com/problems/remove-element/
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while True:
            try:
                nums.remove(val)
            except ValueError:
                return len(nums)


if __name__ == "__main__":
    nums = [3,2,2,3]        # Input array
    val = 3                 # Value to remove
    expectedNums = [2,2]    # The expected answer with correct length

    k = Solution().removeElement(nums, val)  # Calls your implementation
    expectedNums.sort()
    nums.sort()
    print(nums)

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]


    nums = [0,1,2,2,3,0,4,2]        # Input array
    val = 2                         # Value to remove
    expectedNums = [0,1,4,0,3]      # The expected answer with correct length

    k = Solution().removeElement(nums, val)  # Calls your implementation
    expectedNums.sort()
    nums.sort()
    print(nums)

    assert k == len(expectedNums)
    for i in range(k):
        assert nums[i] == expectedNums[i]
