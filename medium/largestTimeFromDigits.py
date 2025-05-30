# https://leetcode.com/problems/largest-time-for-given-digits/

from typing import List


class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        result = []
        arr.sort(reverse=True)

        def backtrack(path: list[int]):
            if (len(path) == 2 and path[0] * 10 + path[1] > 23) or (len(path) == 4 and path[2] * 10 + path[3] > 59):
                return
            if len(path) == len(arr):
                result.append(path[:])
                return
            for i in range(len(arr)):
                if arr[i] > -1:
                    path.append(arr[i])
                    tmp, arr[i] = arr[i], -1
                    backtrack(path)
                    path.pop()
                    arr[i] = tmp

        backtrack([])
        return f"{result[0][0]}{result[0][1]}:{result[0][2]}{result[0][3]}" if result else ""


if __name__ == "__main__":
    solution = Solution()

    def check_case(arr: List[int], expected: str):
        result = solution.largestTimeFromDigits(arr)
        assert result == expected, f"Failed for input: {arr}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case([1, 2, 3, 4], "23:41")

    # Пример 2
    check_case([5, 5, 5, 5], "")

    # Пример 3
    check_case([0, 0, 0, 0], "00:00")

    print("All test cases passed.")
