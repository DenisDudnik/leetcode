# https://leetcode.com/problems/non-decreasing-subsequences/

from typing import List


class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return []

        result = []

        def backtrack(start: int, path: list[int]):
            if len(path) > 1:
                result.append(path[:])

            used = set()
            for i in range(start, len(nums)):
                if nums[i] in used:
                    continue
                if path and path[-1] > nums[i]:
                    continue
                path.append(nums[i])
                used.add(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return result


# --- Тесты из условия задачи ---
sol = Solution()

# Test case 1
nums = [4, 6, 7, 7]
expected_output = [[4, 6], [4, 6, 7], [4, 6, 7, 7], [4, 7], [4, 7, 7], [6, 7], [6, 7, 7], [7, 7]]
result = sol.findSubsequences(nums)
assert sorted(result) == sorted(expected_output), f"Test 1 failed: {result}"

# Test case 2
nums = [4, 4, 3, 2, 1]
expected_output = [[4, 4]]
result = sol.findSubsequences(nums)
assert sorted(result) == sorted(expected_output), f"Test 2 failed: {result}"

# Test case 3
nums = [4, 4, 5, 2, 1]
expected_output = [[4, 4], [4, 4, 5], [4, 5]]
result = sol.findSubsequences(nums)
assert sorted(result) == sorted(expected_output), f"Test 3 failed: {result}"

print("All tests passed.")
