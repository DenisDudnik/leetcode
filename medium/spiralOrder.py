# https://leetcode.com/problems/spiral-matrix/

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 1:
            return matrix[0]

        count = len(matrix) * len(matrix[0])
        res = []
        left, right, top, bottom = -1, len(matrix[0]), -1, len(matrix)
        x, y = 0, 0
        h, v = 1, 0

        while count:
            res.append(matrix[y][x])
            count -= 1
            if h > 0 and x + h == right:
                h = 0
                v = 1
                top += 1
            elif h < 0 and x + h == left:
                h = 0
                v = -1
                bottom -= 1
            elif v > 0 and y + v == bottom:
                h = -1
                v = 0
                right -= 1
            elif v < 0 and y + v == top:
                h = 1
                v = 0
                left += 1
            x += h
            y += v
        return res


if __name__ == "__main__":
    assert Solution().spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [
        1,
        2,
        3,
        6,
        9,
        8,
        7,
        4,
        5,
    ]
    assert Solution().spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]) == [
        1,
        2,
        3,
        4,
        8,
        12,
        11,
        10,
        9,
        5,
        6,
        7,
    ]
