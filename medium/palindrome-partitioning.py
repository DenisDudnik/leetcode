# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

# 2025-11-04
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[None] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                if j - i <= 2:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = s[i] == s[j] and dp[i + 1][j - 1]

        result = []

        def backtrack(path: list[str], left: int):
            if left == n:
                result.append(path[:])
                return

            for right in range(left, n):
                if dp[left][right]:
                    path.append(s[left : right + 1])
                    backtrack(path, right + 1)
                    path.pop()

        backtrack([], 0)
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
assert sorted(sol.partition("efe")) == sorted([["e", "f", "e"], ["efe"]])
assert sorted(sol.partition("abbab")) == sorted(
    [["a", "b", "b", "a", "b"], ["a", "b", "bab"], ["a", "bb", "a", "b"], ["abba", "b"]]
)
