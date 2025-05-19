# https://leetcode.com/problems/letter-case-permutation/

from typing import List


class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []

        def backtrack(pos: int, path: str):
            if pos == len(s):
                result.append(path)
                return
            if s[pos].isalpha():
                backtrack(pos + 1, path + s[pos].upper())
                backtrack(pos + 1, path + s[pos].lower())
            else:
                backtrack(pos + 1, path + s[pos])

        backtrack(0, "")
        return result


# Тесты из условия задачи
if __name__ == "__main__":
    solution = Solution()

    # Пример 1
    s1 = "a1b2"
    expected1 = {"a1b2", "a1B2", "A1b2", "A1B2"}
    result1 = set(solution.letterCasePermutation(s1))
    assert result1 == expected1, f"Test case 1 failed: got {result1}"

    # Пример 2
    s2 = "3z4"
    expected2 = {"3z4", "3Z4"}
    result2 = set(solution.letterCasePermutation(s2))
    assert result2 == expected2, f"Test case 2 failed: got {result2}"

    # Дополнительный тест
    s3 = "12345"
    expected3 = {"12345"}
    result3 = set(solution.letterCasePermutation(s3))
    assert result3 == expected3, f"Test case 3 failed: got {result3}"

    print("All test cases passed.")
