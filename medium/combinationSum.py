# https://leetcode.com/problems/combination-sum/

from typing import List


# 2026-02-15
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if target < 2:
            return []

        res = []

        def backtrack(path: list[int], path_sum: int, idx: int):
            if path_sum == target:
                res.append(path[:])
                return
            for i in range(idx, len(candidates)):
                c = candidates[i]
                if path_sum + c <= target:
                    path.append(c)
                    backtrack(path, path_sum + c, i)
                    path.pop()

        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    # Тесты по условиям задачи
    s = Solution()

    # Пример 1
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 6, 7], 7)]) == sorted([[2, 2, 3], [7]])

    # Пример 2
    assert sorted([sorted(x) for x in s.combinationSum([2, 3, 5], 8)]) == sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]])

    # Пример 3
    assert s.combinationSum([2], 1) == []
