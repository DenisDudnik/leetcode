# https://leetcode.com/problems/game-of-life/


from collections import Counter
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        idxs_for_change = []
        m = len(board)
        n = len(board[0])

        for i in range(m):
            for j in range(n):
                neighbors = []
                top, bottom, left, right = i - 1, i + 1, j - 1, j + 1
                if i == 0:
                    top += 1
                if i == m - 1:
                    bottom -= 1
                if j == 0:
                    left += 1
                if j == n - 1:
                    right -= 1

                for v in range(top, bottom + 1):
                    for h in range(left, right + 1):
                        if not (v == i and h == j):
                            neighbors.append(board[v][h])
                neighbors_counter = Counter(neighbors)
                print(f"{i=}, {j=}, {neighbors_counter=}, {neighbors=}")

                if (
                    board[i][j] == 1
                    and (neighbors_counter[1] < 2 or neighbors_counter[1] > 3)
                ) or (board[i][j] == 0 and neighbors_counter[1] == 3):
                    idxs_for_change.append((i, j))

        for i, j in idxs_for_change:
            board[i][j] = 1 if board[i][j] == 0 else 0

        print(f"{idxs_for_change=}")
        print(f"{board=}")


if __name__ == "__main__":
    # board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
    # Solution().gameOfLife(board)
    # assert board == [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]

    # board = [[1, 1], [1, 0]]
    # Solution().gameOfLife(board)
    # assert board == [[1, 1], [1, 1]]

    board = [[0]]
    Solution().gameOfLife(board)
    assert board == [[0]]
