# https://leetcode.com/problems/target-sum/

from functools import lru_cache
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @lru_cache(maxsize=None)
        def backtrack(i: int, path_sum: int) -> int:
            if i == n:
                if path_sum == target:
                    return 1
                return 0

            res_1 = backtrack(i + 1, path_sum + nums[i])
            res_2 = backtrack(i + 1, path_sum - nums[i])

            return res_1 + res_2

        result = backtrack(0, 0)
        print(result)
        return result


# Примеры из условия задачи
if __name__ == "__main__":
    solution = Solution()

    # Пример 1
    nums1 = [1, 1, 1, 1, 1]
    target1 = 3
    expected1 = 5
    assert solution.findTargetSumWays(nums1, target1) == expected1, "Test 1 failed"

    # Пример 2
    nums2 = [1]
    target2 = 1
    expected2 = 1
    assert solution.findTargetSumWays(nums2, target2) == expected2, "Test 2 failed"

    # Пример 3
    nums3 = [0, 0, 0, 0, 0, 0, 0, 0, 1]
    target3 = 1
    expected3 = 256
    assert solution.findTargetSumWays(nums3, target3) == expected3, "Test 3 failed"

    # Пример 4
    nums4 = [19, 24, 2, 28, 27, 49, 6, 45, 20, 45, 34, 19, 5, 0, 39, 24, 48, 1, 44, 23]
    target4 = 10
    expected4 = 6056
    assert solution.findTargetSumWays(nums4, target4) == expected4, "Test 4 failed"

    print("All tests passed.")
