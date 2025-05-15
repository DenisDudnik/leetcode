# https://leetcode.com/problems/combinations/

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        nums = list(range(1, n + 1))
        result = []

        def backtrack(start: int, path: list[int]):
            if len(path) == k:
                result.append(path[:])
                return
            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


# ✅ Тесты из условия задачи
s = Solution()

assert sorted(s.combine(4, 2)) == sorted([[2, 4], [3, 4], [2, 3], [1, 2], [1, 3], [1, 4]])

assert sorted(s.combine(1, 1)) == [[1]]

print("All test cases passed.")
