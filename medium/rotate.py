# https://leetcode.com/problems/rotate-array/

from typing import List

# 2025-12-28
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        if k == 0:
            return

        def rotate_nums(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        rotate_nums(0, len(nums) - 1)
        rotate_nums(0, k - 1)
        rotate_nums(k, len(nums) - 1)


if __name__ == "__main__":
    nums, k = [1, 2, 3, 4, 5, 6, 7], 4
    Solution().rotate(nums=nums, k=k)
    assert nums == [4, 5, 6, 7, 1, 2, 3]

    nums, k = [-1, -100, 3, 99], 2
    Solution().rotate(nums=nums, k=k)
    assert nums == [3, 99, -1, -100]

    nums, k = [1, 2], 3
    Solution().rotate(nums=nums, k=k)
    assert nums == [2, 1]
