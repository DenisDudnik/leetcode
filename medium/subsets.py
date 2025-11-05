# https://leetcode.com/problems/subsets/

from typing import List


# 2025-11-04
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(path: list[int], idx: int):
            result.append(path[:])

            if idx == len(nums):
                return

            for i in range(idx, len(nums)):
                path.append(nums[i])
                backtrack(path, i + 1)
                path.pop()

        backtrack([], 0)
        return result


# Тесты
if __name__ == "__main__":
    solution = Solution()

    # Тест 1: nums = [1, 2, 3]
    result_1 = solution.subsets([1, 2, 3])
    expected_1 = [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    assert sorted(result_1) == sorted(expected_1), f"Test 1 failed: {result_1}"

    # Тест 2: nums = [0]
    result_2 = solution.subsets([0])
    expected_2 = [[], [0]]
    assert sorted(result_2) == sorted(expected_2), f"Test 2 failed: {result_2}"

    # Тест 3: nums = [1]
    result_3 = solution.subsets([1])
    expected_3 = [[], [1]]
    assert sorted(result_3) == sorted(expected_3), f"Test 3 failed: {result_3}"

    print("All tests passed!")
