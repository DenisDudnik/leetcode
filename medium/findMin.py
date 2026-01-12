# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


# 2026-01-12
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            if nums[left] <= nums[right]:
                return nums[left]

            mid = (left + right) // 2

            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid



if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], expected: int):
        result = solution.findMin(nums)
        assert result == expected, f"Failed: nums={nums}, expected={expected}, got={result}"

    # Пример 1
    check_case([3, 4, 5, 1, 2], 1)

    # Пример 2
    check_case([4, 5, 6, 7, 8, 0, 1, 2], 0)

    # Пример 3
    check_case([11, 13, 15, 17], 11)

    # Без поворота
    check_case([1, 2, 3, 4, 5], 1)

    print("All test cases passed.")
