# https://leetcode.com/problems/set-matrix-zeroes/

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        cols, rows = set(), set()
        m = len(matrix)
        n = len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    cols.add(j)
                    rows.add(i)
        
        for i in rows:
            for j in range(n):
                matrix[i][j] = 0
                
        for j in cols:
            for i in range(m):
                matrix[i][j] = 0
        
        print(matrix)


if __name__ == "__main__":
    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    Solution().setZeroes(matrix)
    assert matrix == [[1,0,1],[0,0,0],[1,0,1]]

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    Solution().setZeroes(matrix)
    assert matrix == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
