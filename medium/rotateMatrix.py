# https://leetcode.com/problems/rotate-image/

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # x, y = 0, 0
        # val = matrix[x][y]
        # seen = set()
        # size = len(matrix)
        # count = len(matrix) ** 2
        # while len(seen) < count:
        #     if (x, y) in seen:
        #         if y + 1 < size:
        #             y += 1
        #         else:
        #             y = 0
        #             x = (x + 1) % size
        #         val = matrix[x][y]
        #         continue
        #     seen.add((x, y))
        #     val, matrix[y][size - 1 - x] = matrix[y][size - 1 - x], val
        #     x, y = y, size - 1 - x
        
        size = len(matrix)
        top, bottom = 0, size - 1
        
        while top < bottom:
            matrix[top], matrix[bottom] = matrix[bottom], matrix[top]
            top += 1
            bottom -= 1
        
        for i in range(size):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        print(matrix)


if __name__ == "__main__":
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Solution().rotate(matrix)
    assert matrix == [[7,4,1],[8,5,2],[9,6,3]]

    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    Solution().rotate(matrix)
    assert matrix == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
