# https://leetcode.com/problems/combination-sum-iii/

from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result = []

        if sum(range(1, k + 1)) > n:
            return result

        def backtrack(start: int, path: list[int], path_sum: int):
            if len(path) == k:
                if path_sum == n:
                    result.append(path[:])
                return
            for i in range(start, 10):
                if path_sum + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, path_sum + i)
                path.pop()

        backtrack(1, [], 0)
        return result


# 🧪 Тесты из описания задачи
sol = Solution()

assert sorted(sol.combinationSum3(3, 7)) == sorted([[1, 2, 4]])
assert sorted(sol.combinationSum3(3, 9)) == sorted([[1, 2, 6], [1, 3, 5], [2, 3, 4]])
assert sorted(sol.combinationSum3(4, 1)) == sorted([])  # Сумму 1 невозможно набрать с 4 уникальными числами 1–9
