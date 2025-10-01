# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


# 2025-10-01
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        dp = [[None] * len(s) for _ in range(len(s))]

        for j in range(len(s)):
            for i in range(len(s)):
                if j < i:
                    break
                elif j - i < 2:
                    dp[j][i] = s[i] == s[j]
                else:
                    dp[j][i] = (s[i] == s[j]) and dp[j - 1][i + 1]

        def is_palindrome(i: int, j: int) -> bool:
            return dp[j-1][i]

        def backtrack(path: list[str], start_idx: int):
            if start_idx == len(s):
                result.append(path[:])
                return
            for i in range(start_idx + 1, len(s) + 1):
                if is_palindrome(start_idx, i):
                    path.append(s[start_idx:i])
                    backtrack(path, i)
                    path.pop()

        backtrack([], 0)
        return result


sol = Solution()

# assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
# assert sorted(sol.partition("a")) == sorted([["a"]])
assert sorted(sol.partition("efe")) == sorted([["e","f","e"],["efe"]])
