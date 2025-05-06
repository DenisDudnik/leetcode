# https://leetcode.com/problems/generate-parentheses/

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtracking(left: int, right: int, combination: str) -> None:
            if len(combination) == 2 * n:
                result.append(combination)
                return

            if left < n:
                backtracking(left + 1, right, combination + "(")
            if right < left:
                backtracking(left, right + 1, combination + ")")

        result = []
        backtracking(0, 0, "")
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
