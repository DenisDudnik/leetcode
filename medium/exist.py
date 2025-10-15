# https://leetcode.com/problems/word-search/

from collections import Counter
from typing import List


# 2025-10-10
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        word_letters = Counter(word)
        board_letters = Counter(c for r in board for c in r)

        for letter in word_letters:
            if word_letters[letter] > board_letters[letter]:
                return False

        if board_letters[word[0]] > board_letters[word[-1]]:
            word = word[::-1]

        def backtrack(row: int, col: int, i: int) -> bool:
            if i == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] == "#" or board[row][col] != word[i]:
                return False

            tmp, board[row][col] = board[row][col], "#"
            res = (
                backtrack(row - 1, col, i + 1)
                or backtrack(row + 1, col, i + 1)
                or backtrack(row, col - 1, i + 1)
                or backtrack(row, col + 1, i + 1)
            )
            board[row][col] = tmp
            return res

        for r in range(rows):
            for c in range(cols):
                if backtrack(r, c, 0):
                    return True

        return False


sol = Solution()

board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

assert sol.exist(board1, "ABCCED") is True, "Test case 1 failed"
assert sol.exist(board1, "SEE") is True, "Test case 2 failed"
assert sol.exist(board1, "ABCB") is False, "Test case 3 failed"
