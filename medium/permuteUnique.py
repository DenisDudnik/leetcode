# https://leetcode.com/problems/permutations-ii/

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        used = [False] * len(nums)
        nums.sort()

        def backtrack(path: list[int]):
            if len(path) == len(nums):
                results.append(path[:])
                return

            for idx in range(len(nums)):
                if used[idx]:
                    continue

                if idx > 0 and nums[idx] == nums[idx - 1] and not used[idx - 1]:
                    continue

                used[idx] = True
                path.append(nums[idx])
                backtrack(path)
                used[idx] = False
                path.pop()

        backtrack([])
        return results


# 🔽 Тесты из условия
s = Solution()

result1 = s.permuteUnique([1, 1, 2])
expected1 = [
    [1, 1, 2],
    [1, 2, 1],
    [2, 1, 1],
]
assert sorted(result1) == sorted(expected1), f"Test case 1 failed: got {result1}"

result2 = s.permuteUnique([1, 2, 3])
expected2 = [
    [1, 2, 3],
    [1, 3, 2],
    [2, 1, 3],
    [2, 3, 1],
    [3, 1, 2],
    [3, 2, 1],
]
assert sorted(result2) == sorted(expected2), f"Test case 2 failed: got {result2}"

result3 = s.permuteUnique([3, 3, 0, 3])
expected3 = [[0, 3, 3, 3], [3, 0, 3, 3], [3, 3, 0, 3], [3, 3, 3, 0]]
assert sorted(result3) == sorted(expected3), f"Test case 3 failed: got {result3}"

print("All test cases passed!")
