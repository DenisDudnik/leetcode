# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/

from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        result = 0
        best_possible_result = sum((len(s) for s in arr))

        def backtrack(idx: int, path: str):
            nonlocal result
            result = max(result, len(path))
            if idx == len(arr) or result == best_possible_result:
                return

            for i in range(idx, len(arr)):
                if i and arr[i] == arr[i-1]:
                    continue
                new_path = path+arr[i]
                if len(new_path) == len(set(new_path)):
                    backtrack(i + 1, new_path)

        backtrack(0, "")
        return result


if __name__ == "__main__":
    solution = Solution()

    def check_case(arr: List[str], expected: int):
        result = solution.maxLength(arr)
        assert result == expected, f"Failed for input: {arr}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case(["un", "iq", "ue"], 4)  # "uniq" или "ique"

    # Пример 2
    check_case(["cha", "r", "act", "ers"], 6)  # "chaers" или "acters"

    # Пример 3
    check_case(["abcdefghijklmnopqrstuvwxyz"], 26)

    # Пример 4
    check_case(["aa", "bb"], 0)  # все элементы содержат дубли

    # Пример 4
    check_case(["jnfbyktlrqumowxd", "mvhgcpxnjzrdei"], 16)

    print("All test cases passed.")
