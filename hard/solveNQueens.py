# https://leetcode.com/problems/n-queens/

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(row: int, used_cols: set[int], diag_1: set[int], diag_2: set[int]):
            if row == n:
                res = ["".join(r) for r in board]
                result.append(res)
                return

            for col in range(n):
                if col in used_cols or row - col in diag_1 or col + row in diag_2:
                    continue
                board[row][col] = "Q"
                used_cols.add(col)
                diag_1.add(row - col)
                diag_2.add(row + col)
                backtrack(row + 1, used_cols, diag_1, diag_2)
                board[row][col] = "."
                used_cols.discard(col)
                diag_1.discard(row - col)
                diag_2.discard(row + col)

        backtrack(0, set(), set(), set())
        return result


# Тесты
s = Solution()

# Пример 1
expected_4 = [[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]
assert sorted(s.solveNQueens(4)) == sorted(expected_4)

# Пример 2
assert s.solveNQueens(1) == [["Q"]]

# Пример 3
expected_5 = [
    ["Q....", "..Q..", "....Q", ".Q...", "...Q."],
    ["Q....", "...Q.", ".Q...", "....Q", "..Q.."],
    [".Q...", "...Q.", "Q....", "..Q..", "....Q"],
    [".Q...", "....Q", "..Q..", "Q....", "...Q."],
    ["..Q..", "Q....", "...Q.", ".Q...", "....Q"],
    ["..Q..", "....Q", ".Q...", "...Q.", "Q...."],
    ["...Q.", "Q....", "..Q..", "....Q", ".Q..."],
    ["...Q.", ".Q...", "....Q", "..Q..", "Q...."],
    ["....Q", ".Q...", "...Q.", "Q....", "..Q.."],
    ["....Q", "..Q..", "Q....", "...Q.", ".Q..."],
]
assert sorted(s.solveNQueens(5)) == sorted(expected_5)
