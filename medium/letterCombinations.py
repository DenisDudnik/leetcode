# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List


# class Solution:
#     def letterCombinations(self, digits: str) -> List[str]:
#         MAPPING = {
#             "2": ["a", "b", "c"],
#             "3": ["d", "e", "f"],
#             "4": ["g", "h", "i"],
#             "5": ["j", "k", "l"],
#             "6": ["m", "n", "o"],
#             "7": ["p", "q", "r", "s"],
#             "8": ["t", "u", "v"],
#             "9": ["w", "x", "y", "z"],
#         }

#         result = MAPPING[digits[0]] if digits else []
#         for digit in digits[1:]:
#             new_res = []
#             for letter in MAPPING[digit]:
#                 for comb in result:
#                     new_res.append(f"{comb}{letter}")
#             result = new_res
#         return result


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        MAPPING = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"],
        }

        def append_letter(idx, combination):
            if idx == len(digits):
                res.append(combination)
                return

            for letter in MAPPING[digits[idx]]:
                append_letter(idx + 1, f"{combination}{letter}")

        if not digits:
            return []

        res = []
        append_letter(0, "")
        return res


if __name__ == "main":
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
