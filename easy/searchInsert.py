# https://leetcode.com/problems/search-insert-position/


from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            med = (left + right) // 2

            if nums[med] < target:
                left = med + 1
            elif nums[med] > target:
                right = med - 1
            else:
                return med

        return left


if __name__ == "__main__":
    solution = Solution()

    def check_case(nums: List[int], target: int, expected: int):
        result = solution.searchInsert(nums, target)
        assert result == expected, (
            f"Failed for input: nums={nums}, target={target}\nExpected: {expected}\nGot: {result}"
        )

    # Пример 1
    check_case([1, 3, 5, 6], 5, 2)

    # Пример 2
    check_case([1, 3, 5, 6], 2, 1)

    # Пример 3
    check_case([1, 3, 5, 6], 7, 4)

    # Пример 4
    check_case([1, 3, 5, 6], 0, 0)

    # Пример 5
    check_case([1], 2, 1)

    # Пример 6
    check_case([1, 3], 3, 1)

    print("All test cases passed.")
