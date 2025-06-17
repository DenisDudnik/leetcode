# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            med = (left + right) // 2

            if nums[med] == target:
                return med

            elif nums[med] >= nums[left]:
                # left sorted
                if nums[med] < target or nums[left] > target:
                    left = med + 1
                else:
                    right = med - 1
            else:
                # right sorted
                if nums[med] > target or nums[right] < target:
                    right = med - 1
                else:
                    left = med + 1

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
    check_case([3,1], 1, 1)

    print("All test cases passed.")
