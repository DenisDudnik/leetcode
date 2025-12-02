# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

# 2025-12-02
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n = len(s)
        dp = [[None] * n for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (j - i <= 2 or dp[i + 1][j - 1]) and s[i] == s[j]

        result = []

        def backtrack(start: int, path: list[str]):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if dp[start][end]:
                    path.append(s[start : end + 1])
                    backtrack(end + 1, path)
                    path.pop()

        backtrack(0, [])
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
assert sorted(sol.partition("efe")) == sorted([["e", "f", "e"], ["efe"]])
assert sorted(sol.partition("abbab")) == sorted(
    [["a", "b", "b", "a", "b"], ["a", "b", "bab"], ["a", "bb", "a", "b"], ["abba", "b"]]
)
