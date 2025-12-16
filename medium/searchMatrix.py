# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


# 2025-12-16
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        first, last = 0, len(matrix) - 1
        row = None

        while first <= last:
            mid = (first + last) // 2
            if target < matrix[mid][0]:
                last = mid - 1
            elif target > matrix[mid][-1]:
                first = mid + 1
            else:
                row = matrix[mid]
                break

        if not row:
            return False

        first, last = 0, len(row) - 1
        while first <= last:
            mid = (first + last) // 2
            if row[mid] == target:
                return True
            elif target < row[mid]:
                last = mid - 1
            else:
                first = mid + 1

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
