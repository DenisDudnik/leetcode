# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


# 2025-09-26
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                # left sorted
                if target > nums[middle] or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            else:
                # right sorted
                if target < nums[middle] or target > nums[right]:
                    right = middle - 1
                else:
                    left = middle + 1

        return -1


if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], target: int, expected: int):
        result = solution.search(nums, target)
        assert result == expected, f"Failed: nums={nums}, target={target}, expected={expected}, got={result}"

    # Пример 1
    check_case([4, 5, 6, 7, 0, 1, 2], 0, 4)

    # Пример 2
    check_case([4, 5, 6, 7, 0, 1, 2], 3, -1)

    # Пример 3
    check_case([1], 0, -1)

    # Пример 4
    check_case([4, 5, 6, 7, 8, 1, 2, 3], 8, 4)

    # Пример 5
    check_case([3, 1], 1, 1)

    print("All test cases passed.")
