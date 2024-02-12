# https://leetcode.com/problems/validate-binary-search-tree/

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        islands, visited = 0, set()

        def bfs(row, col):
            q = deque()
            q.append((row, col))
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            while q:
                r, c = q.popleft()
                for r_dir, c_dir in directions:
                    r_n, c_n = r + r_dir, c + c_dir
                    if (
                        r_n in range(rows)
                        and c_n in range(cols)
                        and grid[r_n][c_n] == "1"
                        and (r_n, c_n) not in visited
                    ):
                        q.append((r_n, c_n))
                        visited.add((r_n, c_n))

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row, col) not in visited:
                    bfs(row, col)
                    islands += 1

        return islands


if __name__ == "__main__":
    # Input: grid = [
    # ["1","1","1","1","0"],
    # ["1","1","0","1","0"],
    # ["1","1","0","0","0"],
    # ["0","0","0","0","0"]
    # ]
    # Output: 1
    grid = [
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"],
    ]
    output = 1

    assert Solution().numIslands(grid) == output
