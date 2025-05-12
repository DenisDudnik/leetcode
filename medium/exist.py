# https://leetcode.com/problems/word-search/

from collections import Counter
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        board_letters = Counter(c for r in board for c in r)
        word_letters = Counter(word)
        if any(board_letters[c] < word_letters[c] for c in word_letters):
            return False

        rows, cols = len(board), len(board[0])

        def backtracking(row, col, idx):
            if idx == len(word):
                return True

            if (
                row < 0
                or row >= rows
                or col < 0
                or col >= cols
                or board[row][col] == "#"
                or board[row][col] != word[idx]
            ):
                return False

            tmp, board[row][col] = board[row][col], "#"
            res = (
                backtracking(row, col - 1, idx + 1)
                or backtracking(row, col + 1, idx + 1)
                or backtracking(row - 1, col, idx + 1)
                or backtracking(row + 1, col, idx + 1)
            )
            board[row][col] = tmp
            return res

        for row in range(rows):
            for col in range(cols):
                if backtracking(row, col, 0):
                    return True
        return False


sol = Solution()

board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

assert sol.exist(board1, "ABCCED") is True, "Test case 1 failed"
assert sol.exist(board1, "SEE") is True, "Test case 2 failed"
assert sol.exist(board1, "ABCB") is False, "Test case 3 failed"
