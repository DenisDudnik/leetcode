# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


# 2025-12-02
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        top, bottom = 0, len(matrix) - 1

        line = None
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
            elif target > matrix[mid][-1]:
                top = mid + 1
            else:
                line = matrix[mid]
                break

        if line is None:
            return False

        left, right = 0, len(line) - 1
        while left <= right:
            mid = (left + right) // 2
            if target == line[mid]:
                return True
            elif target < line[mid]:
                right = mid - 1
            else:
                left = mid + 1

        return False


if __name__ == "__main__":
    solution = Solution()

    def check_case(matrix: List[List[int]], target: int, expected: bool):
        result = solution.searchMatrix(matrix, target)
        assert result == expected, f"Failed: target={target}, expected={expected}, got={result}"

    # Пример 1
    check_case([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3, True)

    # Пример 2
    check_case([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13, False)

    # Пример 3
    check_case([[1], [3]], 2, False)

    # Единичный элемент
    check_case([[1]], 1, True)

    print("All test cases passed.")
