# https://leetcode.com/problems/combination-sum/

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtracking(combination: List[int], comb_sum: int, idx: int) -> None:
            if comb_sum == target:
                result.append(combination)
                return
            if comb_sum > target:
                return
            for idx_next in range(idx, len(candidates)):
                backtracking(combination + [candidates[idx_next]], comb_sum + candidates[idx_next], idx_next)

        backtracking([], 0, 0)
        return list(result)


if __name__ == "__main__":
    # Тесты по условиям задачи
    s = Solution()

    # Пример 1
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 6, 7], 7)]) == sorted([[2, 2, 3], [7]])

    # Пример 2
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 5], 8)]) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    # Пример 3
    assert s.combinationSum([2], 1) == []
