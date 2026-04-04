# https://leetcode.com/problems/rotate-array/

from typing import List


# 2026-03-30
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n

        if k == 0:
            return

        def rotate_list(left: int, right: int):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        rotate_list(0, n - 1)
        rotate_list(0, k - 1)
        rotate_list(k, n - 1)


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
