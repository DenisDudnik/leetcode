# https://leetcode.com/problems/subsets-ii/

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()

        def backtrack(start: int, path: list[int]):
            result.append(path[:])
            if start == len(nums):
                return

            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i-1]:
                    continue

                path.append(nums[i])
                backtrack(i+1, path)
                path.pop()

        backtrack(0, [])
        return result


# 🧪 Тесты из описания задачи
sol = Solution()

assert sorted(sol.subsetsWithDup([1, 2, 2])) == sorted([[], [1], [1, 2], [1, 2, 2], [2], [2, 2]])

assert sorted(sol.subsetsWithDup([0])) == sorted([[], [0]])
