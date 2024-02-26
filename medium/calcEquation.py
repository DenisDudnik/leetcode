# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict
from typing import List


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(dict)

        for (x, y), value in zip(equations, values):
            graph[x][y] = value
            graph[y][x] = 1 / value

        def dfs(x, y, visited):
            if x not in graph or y not in graph:
                return -1

            if y in graph[x]:
                return graph[x][y]

            for i in graph[x]:
                if i not in visited:
                    visited.add(i)
                    temp = dfs(i, y, visited)
                    if temp == -1:
                        continue
                    else:
                        return temp * graph[x][i]
            return -1

        res = [dfs(querie[0], querie[1], set()) for querie in queries]
        print(res)
        return res


if __name__ == "__main__":
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]

    output = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]

    assert Solution().calcEquation(equations, values, queries) == output

    equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
    values = [1.5, 2.5, 5.0]
    queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]

    output = [3.75000, 0.40000, 5.00000, 0.20000]

    assert Solution().calcEquation(equations, values, queries) == output
