# https://leetcode.com/problems/jump-game/description/

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        nums.reverse()
        distance = 1
        for num in nums[1:]:
            if num >= distance:
                distance = 0
            distance += 1
        if distance == 1:
            return True
        return False


if __name__ == "__main__":
    assert Solution().canJump([2,3,1,1,4]) == True
    assert Solution().canJump([3,2,1,0,4]) == False
