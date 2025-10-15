# https://leetcode.com/problems/permutations/

from typing import List


# 2025-10-10
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # result = []
        # used = [False] * len(nums)

        # def backtrack(path: list[int]):
        #     if len(path) == len(nums):
        #         result.append(path[:])
        #         return

        #     for i in range(len(nums)):
        #         if not used[i]:
        #             used[i] = True
        #             path.append(nums[i])
        #             backtrack(path)
        #             path.pop()
        #             used[i] = False

        # backtrack([])
        # return result
        import itertools

        return [list(c) for c in itertools.permutations(nums)]


# Тесты
s = Solution()

# Пример 1
assert sorted(s.permute([1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

# Пример 2
assert sorted(s.permute([0, 1])) == sorted([[0, 1], [1, 0]])

# Пример 3
assert sorted(s.permute([1])) == [[1]]
