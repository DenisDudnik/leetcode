# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

# 2025-12-15
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        # result = []

        # def backtrack(path: list[str], idx: int):
        #     if idx == len(digits):
        #         if path:
        #             result.append("".join(path))
        #         return
        #     for s in MAPPING[digits[idx]]:
        #         path.append(s)
        #         backtrack(path, idx + 1)
        #         path.pop()

        # backtrack([], 0)
        # return result

        import itertools

        source = [MAPPING[d] for d in digits]
        return ["".join(p) for p in itertools.product(*source) if p]


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
