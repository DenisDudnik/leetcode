# https://leetcode.com/problems/palindrome-partitioning/

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_palindrom(word: str):
            return word == word[::-1]

        def backtrack(left: int, path: list):
            if left == len(s):
                result.append(path[:])
                return
            for right in range(left + 1, len(s) + 1):
                word = s[left:right]
                if is_palindrom(word):
                    path.append(word)
                    backtrack(right, path)
                    path.pop()

        backtrack(0, [])
        return result


sol = Solution()

assert sorted(sol.partition("aab")) == sorted([["a", "a", "b"], ["aa", "b"]])
assert sorted(sol.partition("a")) == sorted([["a"]])
