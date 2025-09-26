# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


# 2025-09-26
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        cache = {}

        def is_palindrome(s: str):
            if s not in cache:
                cache[s] = s[0] == s[-1] and s == s[::-1]
            return cache.get(s)

        def backtrack(path: list[str], idx: int):
            if idx == len(s):
                result.append(path[:])
                return

            for i in range(idx + 1, len(s) + 1):
                part = s[idx:i]
                if is_palindrome(part):
                    path.append(part)
                    backtrack(path, i)
                    path.pop()

        backtrack([], 0)
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
