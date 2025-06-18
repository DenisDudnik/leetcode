# https://leetcode.com/problems/search-a-2d-matrix/

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows_cnt = len(matrix)
        cols_cnt = len(matrix[0])
        row_num = -1

        left, right = 0, rows_cnt - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and matrix[mid][-1] >= target:
                row_num = mid
                break

            if matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid + 1

        if row_num == -1:
            return False

        left, right = 0, cols_cnt - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[row_num][mid] == target:
                return True

            if matrix[row_num][mid] > target:
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

    # Единичный элемент
    check_case([[1]], 1, True)

    print("All test cases passed.")
