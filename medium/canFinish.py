# https://leetcode.com/problems/course-schedule/

from collections import defaultdict, deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for (a, b) in prerequisites:
            if a == b:
                return False
            graph[a].append(b)

        visited = set()

        def dfs(course):
            if not graph.get(course):
                return True
            if course in visited:
                return False
            visited.add(course)
            for c in graph[course]:
                if not dfs(c):
                    return False
                graph[c] = []
            visited.remove(course)
            return True

        for k in range(numCourses):
            if not dfs(k):
                return False

        return True


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]

    output = True

    assert Solution().canFinish(numCourses, prerequisites) == output

    print("-------")
    numCourses = 2
    prerequisites = [[1, 0], [0, 1]]

    output = False

    assert Solution().canFinish(numCourses, prerequisites) == output
    print("-------")

    numCourses = 20
    prerequisites = [[0, 10], [3, 18], [5, 5], [6, 11], [11, 14], [13, 1], [15, 1], [17, 4]]

    output = False

    assert Solution().canFinish(numCourses, prerequisites) == output
    print("-------")

    numCourses = 5
    prerequisites = [[1, 4], [2, 4], [3, 1], [3, 2]]

    output = True

    assert Solution().canFinish(numCourses, prerequisites) == output
