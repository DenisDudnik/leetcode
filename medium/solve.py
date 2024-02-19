# https://leetcode.com/problems/surrounded-regions/

from typing import List
from collections import deque


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        bordered_o = []
        visited = set()

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        rows, cols = len(board), len(board[0])
        row, col = 0, 0

        for dir_y, dir_x in directions:
            while True:
                if (row, col) not in visited:
                    visited.add((row, col))
                    if board[row][col] == "O":
                        bordered_o.append((row, col))
                        board[row][col] = "B"
                row += dir_y
                col += dir_x
                if row not in range(rows):
                    row -= dir_y
                    break
                if col not in range(cols):
                    col -= dir_x
                    break

        while bordered_o:
            row, col = bordered_o.pop()
            if (row, col) not in visited:
                visited.add((row, col))
                board[row][col] = "B"
            for dir_y, dir_x in directions:
                row_near, col_near = row + dir_y, col + dir_x
                if row_near in range(rows) and col_near in range(cols) and board[row_near][col_near] == "O":
                    bordered_o.append((row_near, col_near))

        for y in range(rows):
            for x in range(cols):
                if board[y][x] == "O":
                    board[y][x] = "X"
                elif board[y][x] == "B":
                    board[y][x] = "O"


if __name__ == "__main__":
    # Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    # Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    board = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"],
    ]
    output = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"],
    ]

    Solution().solve(board)
    assert board == output
