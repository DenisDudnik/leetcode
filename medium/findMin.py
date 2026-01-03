# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

from typing import List


# class Solution:
#     def findMin(self, nums: List[int]) -> int:
#         if nums[0] <= nums[-1]:
#             return nums[0]

#         left, right = 0, len(nums) - 1
#         min_val = float("inf")

#         while left <= right:
#             mid = (left + right) // 2
#             if nums[mid] < min_val:
#                 min_val = nums[mid]

#             if nums[left] <= nums[right]:
#                 # all sorted
#                 min_val = min(min_val, nums[left])
#                 break

#             if nums[left] <= nums[mid]:
#                 # left is sorted
#                 left = mid + 1
#             else:
#                 # right is sorted
#                 right = mid - 1

#         return min_val


# 2026-01-03
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            if nums[left] < nums[right]:
                return nums[left]

            mid = (left + right) // 2

            # left sorted
            if nums[left] <= nums[mid]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], expected: int):
        result = solution.findMin(nums)
        assert result == expected, f"Failed: nums={nums}, expected={expected}, got={result}"

    # Пример 1
    check_case([3, 4, 5, 1, 2], 1)

    # Пример 2
    check_case([4, 5, 6, 7, 0, 1, 2], 0)

    # Пример 3
    check_case([11, 13, 15, 17], 11)

    # Без поворота
    check_case([1, 2, 3, 4, 5], 1)

    print("All test cases passed.")
