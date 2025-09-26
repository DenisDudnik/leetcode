# https://leetcode.com/problems/generate-parentheses/

from typing import List


# 2025-09-26
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path: list[str], left: int, right: int):
            if right == n:
                result.append("".join(path))
                return
            if left < n:
                backtrack(path + ["("], left + 1, right)
            if right < left:
                backtrack(path + [")"], left, right + 1)

        backtrack([], 0, 0)
        return result


if __name__ == "__main__":
    # Тесты по условиям задачи
    s = Solution()

    # Пример 1: n = 1 → одна пара скобок
    assert sorted(s.generateParenthesis(1)) == sorted(["()"])

    # Пример 2: n = 2 → две пары скобок
    assert sorted(s.generateParenthesis(2)) == sorted(["(())", "()()"])

    # Пример 3: n = 3 → пять возможных правильных комбинаций
    assert sorted(s.generateParenthesis(3)) == sorted(["((()))", "(()())", "(())()", "()(())", "()()()"])
