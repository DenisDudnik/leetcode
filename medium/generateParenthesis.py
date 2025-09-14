# https://leetcode.com/problems/generate-parentheses/

from typing import List


# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         def backtracking(left: int, right: int, combination: str) -> None:
#             if len(combination) == 2 * n:
#                 result.append(combination)
#                 return

#             if left < n:
#                 backtracking(left + 1, right, combination + "(")
#             if right < left:
#                 backtracking(left, right + 1, combination + ")")

#         result = []
#         backtracking(0, 0, "")
#         return result


# 2025-09-04
# class Solution:
#     def generateParenthesis(self, n: int) -> List[str]:
#         result = []

#         def backtrack(left: int, right: int, comb: list[str]):
#             if left == n and right == n:
#                 result.append("".join(comb))
#                 return
#             if left < n:
#                 comb.append("(")
#                 backtrack(left + 1, right, comb)
#                 comb.pop()
#             if right < n and right < left:
#                 comb.append(")")
#                 backtrack(left, right + 1, comb)
#                 comb.pop()

#         backtrack(0, 0, [])
#         return result


# 2025-09-14
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def backtrack(path: list[str], left: int, right: int):
            if left == right and right == n:
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
