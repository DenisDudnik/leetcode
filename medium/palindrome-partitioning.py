# https://leetcode.com/problems/palindrome-partitioning/

from typing import List

# 2025-10-15
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        len_s = len(s)
        dp = [[None] * len_s for _ in range(len_s)]

        for i in range(len_s):
            for j in range(len_s):
                if j > i:
                    break
                if i == j or (i - j == 1 and s[i] == s[j]):
                    dp[i][j] = True
                elif s[i] == s[j] and dp[i - 1][j + 1]:
                    dp[i][j] = True
                else:
                    dp[i][j] = False

        def is_palindrome(i, j) -> bool:
            return dp[j][i]

        result = []

        def backtrack(path: list[str], idx: int):
            if idx == len_s:
                result.append(path[:])
                return
            for i in range(idx, len_s):
                if is_palindrome(idx, i):
                    path.append(s[idx : i + 1])
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
assert sorted(sol.partition("efe")) == sorted([["e", "f", "e"], ["efe"]])
assert sorted(sol.partition("abbab")) == sorted([["a","b","b","a","b"],["a","b","bab"],["a","bb","a","b"],["abba","b"]])
