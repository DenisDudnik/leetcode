# https://leetcode.com/problems/numbers-with-same-consecutive-differences/

from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        result = []
        if k == 0:
            start = int("1" * n)
            for i in range(1, 10):
                result.append(start * i)
            return result

        def backtrack(path: list[int], number: int):
            if len(path) == n:
                result.append(number)
                return

            if not path:
                for num in range(1, 10):
                    path.append(num)
                    backtrack(path, num)
                    path.pop()
            else:
                if path[-1] - k >= 0:
                    path.append(path[-1] - k)
                    backtrack(path, number * 10 + path[-1])
                    path.pop()
                if path[-1] + k < 10:
                    path.append(path[-1] + k)
                    backtrack(path, number * 10 + path[-1])
                    path.pop()

        backtrack([], 0)
        return result


if __name__ == "__main__":
    solution = Solution()

    def check_case(n: int, k: int, expected: List[int]):
        result = solution.numsSameConsecDiff(n, k)
        assert sorted(result) == sorted(expected), (
            f"Failed for input: n={n}, k={k}\nExpected: {expected}\nGot: {result}"
        )

    # Пример 1
    check_case(3, 7, [181, 292, 707, 818, 929])

    # Пример 2
    check_case(2, 1, [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98])

    print("All test cases passed.")
