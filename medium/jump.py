# https://leetcode.com/problems/jump-game-ii/

from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        idx, jumps = 0, 0
        while idx < len(nums)-1:
            jumps += 1
            if idx+nums[idx] >= len(nums)-1:
                break
            next_best_idx = idx + 1
            for step in range(1, nums[idx]+1):
                if nums[idx+step] + idx + step >= nums[next_best_idx] + next_best_idx:
                    next_best_idx = idx + step
            idx = next_best_idx
        return jumps


if __name__ == "__main__":
    assert Solution().jump([2,3,1,1,4]) == 2
    assert Solution().jump([2,3,0,1,4]) == 2
    assert Solution().jump([2,1]) == 1
    assert Solution().jump([3,2,1]) == 1
    assert Solution().jump([2,3,1]) == 1
