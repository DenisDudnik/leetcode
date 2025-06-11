# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/


class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        result = []
        chars = "abc"

        def backtrack(path: list[str]):
            if len(path) == n:
                result.append("".join(path))
                return
            for char in chars:
                if len(result) >= k:
                    return
                if not path or (path and char != path[-1]):
                    path.append(char)
                    backtrack(path)
                    path.pop()

        backtrack([])
        return result[k - 1] if len(result) >= k else ""


if __name__ == "__main__":
    solution = Solution()

    def check_case(n: int, k: int, expected: str):
        result = solution.getHappyString(n, k)
        assert result == expected, f"Failed for input: n={n}, k={k}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case(1, 3, "c")

    # Пример 2
    check_case(1, 4, "")  # только 3 возможных happy-строки длины 1

    # Пример 3
    check_case(3, 9, "cab")

    print("All test cases passed.")
