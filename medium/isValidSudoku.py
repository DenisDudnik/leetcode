# https://leetcode.com/problems/valid-sudoku/

from typing import List
from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # replaced_board = [[el for el in line if el != "."] for line in board]
        # for line in replaced_board:
        #     if len(line) != len(set(line)):
        #         return False

        # t_board = list(zip(*board))
        # replaced_board = [[el for el in line if el != "."] for line in t_board]
        # for line in replaced_board:
        #     if len(line) != len(set(line)):
        #         return False

        # for i in range(0, 7, 3):
        #     for j in range(0, 7, 3):
        #         els = []
        #         for x in range(3):
        #             els.extend(board[i+x][j:j+3])
        #         if len([x for x in els if x != "."]) != len(set([x for x in els if x != "."])):
        #             return False
        # return True

        lines = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                if (
                    board[i][j] in lines[i]
                    or board[i][j] in cols[j]
                    or board[i][j] in boxes[i // 3 * 3 + j // 3]
                ):
                    return False
                lines[i].add(board[i][j])
                cols[j].add(board[i][j])
                boxes[i // 3 * 3 + j // 3].add(board[i][j])
        return True


if __name__ == "__main__":
    board = [
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution().isValidSudoku(board) == True

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution().isValidSudoku(board) == False

    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["5", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ]
    assert Solution().isValidSudoku(board) == False
