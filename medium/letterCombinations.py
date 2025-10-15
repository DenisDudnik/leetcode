# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

# 2025-10-10
# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         MAPPING = {
#             "2": "abc",
#             "3": "def",
#             "4": "ghi",
#             "5": "jkl",
#             "6": "mno",
#             "7": "pqrs",
#             "8": "tuv",
#             "9": "wxyz",
#         }

#         result = []

#         def backtrack(path: list[str], idx: int):
#             if idx == len(digits):
#                 if path:
#                     result.append("".join(path))
#                 return
#             letters = MAPPING[digits[idx]]
#             for letter in letters:
#                 path.append(letter)
#                 backtrack(path, idx + 1)
#                 path.pop()

#         backtrack([], 0)
#         return result


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        import itertools

        MAPPING = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combs = [MAPPING[digit] for digit in digits]
        products = itertools.product(*combs)
        result = ["".join(pr) for pr in products if pr]
        return result


if __name__ == "__main__":
    # Тесты по условиям задачи
    s = Solution()

    # Пример 1: Вход "23" -> возможны 9 комбинаций
    assert sorted(s.letterCombinations("23")) == sorted(["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"])

    # Пример 2: Пустая строка -> должен вернуть пустой список
    assert s.letterCombinations("") == []

    # Пример 3: Вход "2" -> три буквы
    assert sorted(s.letterCombinations("2")) == sorted(["a", "b", "c"])

    # Дополнительный: Вход "7" (имеет 4 буквы) -> четыре комбинации
    assert sorted(s.letterCombinations("7")) == sorted(["p", "q", "r", "s"])
