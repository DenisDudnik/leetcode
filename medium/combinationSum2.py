# https://leetcode.com/problems/combination-sum-ii/

from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []

        def backtrack(left: int, path: list[int], path_sum: int):
            if path_sum == target:
                result.append(path[:])
                return
            for i in range(left, len(candidates)):
                if i > left and candidates[i] == candidates[i-1]:
                    continue
                if path_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(i + 1, path, path_sum + candidates[i])
                path.pop()

        backtrack(0, [], 0)
        return result


# 🔍 Тесты из описания задачи
sol = Solution()

# Пример 1
candidates = [10, 1, 2, 7, 6, 1, 5]
target = 8
expected = [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]
output = sol.combinationSum2(candidates, target)
assert sorted([sorted(comb) for comb in output]) == sorted([sorted(comb) for comb in expected]), (
    f"Test 1 failed: {output}"
)

# Пример 2
candidates = [2, 5, 2, 1, 2]
target = 5
expected = [[1, 2, 2], [5]]
output = sol.combinationSum2(candidates, target)
assert sorted([sorted(comb) for comb in output]) == sorted([sorted(comb) for comb in expected]), (
    f"Test 2 failed: {output}"
)

# Пример 3
candidates = [3,1,3,5,1,1]
target = 8
expected = [[1,1,1,5],[1,1,3,3],[3,5]]
output = sol.combinationSum2(candidates, target)
assert sorted([sorted(comb) for comb in output]) == sorted([sorted(comb) for comb in expected]), (
    f"Test 3 failed: {output}"
)
