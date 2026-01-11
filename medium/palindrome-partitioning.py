# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

# 2026-01-10
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)

        dp = [[None] * n for _ in range(n)]

        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (j - i <= 1 or dp[i + 1][j - 1]) and s[i] == s[j]

        def backtrack(path: list[str], start: int):
            if start == n:
                res.append(path[:])
                return

            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start : end + 1])
                    backtrack(path, end + 1)
                    path.pop()

        backtrack([], 0)
        return res


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
assert sorted(sol.partition("efe")) == sorted([["e", "f", "e"], ["efe"]])
assert sorted(sol.partition("abbab")) == sorted(
    [["a", "b", "b", "a", "b"], ["a", "b", "bab"], ["a", "bb", "a", "b"], ["abba", "b"]]
)
