# https://leetcode.com/problems/split-a-string-into-the-max-number-of-unique-substrings/


class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        self.result = 1

        def backtrack(idx: int, path: set[str]):
            if idx == len(s):
                self.result = max(self.result, len(path))
                return

            max_possible_len = len(s) - idx + len(path)
            if max_possible_len <= self.result:
                return

            for i in range(idx, len(s)):
                sub_str = s[idx : i + 1]
                if sub_str in path:
                    continue
                path.add(sub_str)
                backtrack(i + 1, path)
                path.remove(sub_str)

        backtrack(0, set())
        return self.result


if __name__ == "__main__":
    solution = Solution()

    def check_case(s: str, expected: int):
        result = solution.maxUniqueSplit(s)
        assert result == expected, f"Failed for input: {s}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case("ababccc", 5)  # "a", "b", "ab", "c", "cc" — один из вариантов

    # Пример 2
    check_case("aba", 2)  # "a", "ba" или "ab", "a"

    # Пример 3
    check_case("aa", 1)  # только одна уникальная подстрока возможна

    print("All test cases passed.")
