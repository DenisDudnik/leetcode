# https://leetcode.com/problems/permutations/

from typing import List


# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         result = []

#         def backtrack(comb: list[int], used_nums: set):
#             if len(comb) == len(nums):
#                 result.append(comb)
#                 return
#             for num in nums:
#                 if num in used_nums:
#                     continue
#                 backtrack(comb + [num], used_nums.union([num]))

#         backtrack([], set())
#         return result


# 2025-09-08
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        used = [False] * len(nums)

        def backtrack(comb: list[int]):
            if len(comb) == len(nums):
                result.append(comb[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = True
                backtrack(comb + [nums[i]])
                used[i] = False

        backtrack([])
        return result


# Тесты
s = Solution()

# Пример 1
assert sorted(s.permute([1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])

# Пример 2
assert sorted(s.permute([0, 1])) == sorted([[0, 1], [1, 0]])

# Пример 3
assert sorted(s.permute([1])) == [[1]]
