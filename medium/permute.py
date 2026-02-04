# https://leetcode.com/problems/permutations/

from typing import List


# 2026-02-04
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # used = [False] * len(nums)

        # def backtrack(path: list[int]):
        #     if len(path) == len(nums):
        #         res.append(path[:])
        #         return

        #     for i in range(len(nums)):
        #         if not used[i]:
        #             used[i] = True
        #             path.append(nums[i])
        #             backtrack(path)
        #             path.pop()
        #             used[i] = False

        # backtrack([])
        # return res

        from itertools import permutations

        return [list(p) for p in permutations(nums)]


# Тесты
s = Solution()

# Пример 1
assert sorted(s.permute([1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

# Пример 2
assert sorted(s.permute([0, 1])) == sorted([[0, 1], [1, 0]])

# Пример 3
assert sorted(s.permute([1])) == [[1]]
