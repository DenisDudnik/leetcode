# https://leetcode.com/problems/equal-row-and-column-pairs/
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        grid_t = []
        for idx in range(grid_size):
            row = [grid[col][idx] for col in range(grid_size)]
            grid_t.append(row)
        
        pairs = 0
        for idx in range(grid_size):
            pairs += grid_t.count(grid[idx])
        return(pairs)


if __name__ == "__main__":
    assert Solution().equalPairs(grid = [[3,2,1],[1,7,6],[2,7,7]]) == 1
    assert Solution().equalPairs(grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]) == 3


# Amazing answer here: https://leetcode.com/problems/equal-row-and-column-pairs/solutions/2328910/python3-3-lines-transpose-ctr-w-explanation-t-m-100-100/