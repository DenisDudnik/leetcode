# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

from typing import List


# 2025-12-19
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first, last = -1, -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        if first == -1:
            return [-1, -1]

        left, right = first, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return [first, last]


if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], target: int, expected: List[int]):
        result = solution.searchRange(nums, target)
        assert result == expected, (
            f"Failed for input: nums={nums}, target={target}\nExpected: {expected}\nGot: {result}"
        )

    # Пример 1
    check_case([5, 7, 7, 8, 8, 10], 8, [3, 4])

    # Пример 2
    check_case([5, 7, 7, 8, 8, 10], 6, [-1, -1])

    # Пример 3
    check_case([], 0, [-1, -1])

    # Пример 4
    check_case([2, 2], 2, [0, 1])

    print("All test cases passed.")
