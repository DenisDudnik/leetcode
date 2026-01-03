# https://leetcode.com/problems/search-a-2d-matrix-ii/

from typing import List


# 2026-01-03
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        row, col = 0, cols - 1

        while row < rows and col >= 0:
            if matrix[row][col] == target:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1

        return False


# tests
s = Solution()
assert s.searchMatrix(
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ],
    5,
)

assert not s.searchMatrix(
    [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ],
    20,
)
