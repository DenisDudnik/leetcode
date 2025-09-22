# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


# 2025-09-22
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s: str) -> bool:
            return s == s[::-1]

        result = []

        def backtrack(left_idx: int, path: list[str]):
            if left_idx == len(s):
                result.append(path[:])
                return

            for right_idx in range(left_idx + 1, len(s) + 1):
                if is_palindrome(s[left_idx:right_idx]):
                    path.append(s[left_idx:right_idx])
                    backtrack(right_idx, path)
                    path.pop()

        backtrack(0, [])
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
