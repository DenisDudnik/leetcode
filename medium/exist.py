# https://leetcode.com/problems/word-search/

from collections import Counter
from typing import List


# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         board_letters = Counter(c for r in board for c in r)
#         word_letters = Counter(word)
#         if any(board_letters[c] < word_letters[c] for c in word_letters):
#             return False

#         rows, cols = len(board), len(board[0])

#         def backtracking(row, col, idx):
#             if idx == len(word):
#                 return True

#             if (
#                 row < 0
#                 or row >= rows
#                 or col < 0
#                 or col >= cols
#                 or board[row][col] == "#"
#                 or board[row][col] != word[idx]
#             ):
#                 return False

#             tmp, board[row][col] = board[row][col], "#"
#             res = (
#                 backtracking(row, col - 1, idx + 1)
#                 or backtracking(row, col + 1, idx + 1)
#                 or backtracking(row - 1, col, idx + 1)
#                 or backtracking(row + 1, col, idx + 1)
#             )
#             board[row][col] = tmp
#             return res

#         for row in range(rows):
#             for col in range(cols):
#                 if backtracking(row, col, 0):
#                     return True
#         return False


# 2025-09-22
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word_letters = Counter(word)
        board_letters = Counter(c for r in board for c in r)
        if any(word_letters[w] > board_letters[w] for w in word_letters):
            return False

        if board_letters[word[0]] > board_letters[word[-1]]:
            word = word[::-1]

        rows = len(board)
        cols = len(board[0])

        def backtrack(i: int, row: int, col: int):
            if i == len(word):
                return True

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[i] or board[row][col] == ".":
                return False

            temp, board[row][col] = board[row][col], "."

            result = (
                backtrack(i + 1, row + 1, col)
                or backtrack(i + 1, row - 1, col)
                or backtrack(i + 1, row, col + 1)
                or backtrack(i + 1, row, col - 1)
            )

            board[row][col] = temp
            return result

        for r in range(rows):
            for c in range(cols):
                if backtrack(0, r, c):
                    return True

        return False


sol = Solution()

board1 = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]

# assert sol.exist(board1, "ABCCED") is True, "Test case 1 failed"
assert sol.exist(board1, "SEE") is True, "Test case 2 failed"
assert sol.exist(board1, "ABCB") is False, "Test case 3 failed"
