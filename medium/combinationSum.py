# https://leetcode.com/problems/combination-sum/

from typing import List


# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         result = []

#         def backtracking(combination: List[int], comb_sum: int, idx: int) -> None:
#             if comb_sum == target:
#                 result.append(combination)
#                 return
#             if comb_sum > target:
#                 return
#             for idx_next in range(idx, len(candidates)):
#                 backtracking(combination + [candidates[idx_next]], comb_sum + candidates[idx_next], idx_next)

#         backtracking([], 0, 0)
#         return list(result)


# 2025-09-04
# class Solution:
#     def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
#         if target < 2:
#             return []

#         result = []

#         def backtrack(comb: list[int], current: int, start_idx: int):
#             if current == target:
#                 result.append(comb)
#                 return
#             for idx in range(start_idx, len(candidates)):
#                 c = candidates[idx]
#                 if current + c <= target:
#                     backtrack(comb + [c], current + c, idx)

#         backtrack([], 0, 0)
#         return result


# 2025-09-14
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 2:
            return []

        result = []

        def backtrack(path, path_sum, idx: int):
            if path_sum == target:
                result.append(path[:])
                return

            for i in range(idx, len(candidates)):
                c = candidates[i]
                if path_sum + c > target:
                    continue  # if candidates is unsorted, else return
                backtrack(path + [c], path_sum + c, i)

        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    # Тесты по условиям задачи
    s = Solution()

    # Пример 1
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 6, 7], 7)]) == sorted([[2, 2, 3], [7]])

    # Пример 2
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 5], 8)]) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    # Пример 3
    assert s.combinationSum([2], 1) == []
