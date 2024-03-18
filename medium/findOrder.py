# https://leetcode.com/problems/course-schedule-ii/

from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = {c: [] for c in range(numCourses)}
        for c, p in prerequisites:
            graph[c].append(p)
        print(graph)

        colors = {c: 0 for c in range(numCourses)}
        res = []

        def dfs(course):
            if colors[course] == 2:
                return True
            if colors[course] == 1:
                return False
            colors[course] = 1
            for c in graph[course]:
                if not dfs(c):
                    return False
            colors[course] = 2
            res.append(course)
            return True

        for c in graph:
            if not dfs(c):
                return []
        return res


if __name__ == "__main__":
    numCourses = 2
    prerequisites = [[1, 0]]

    output = [[0, 1]]

    assert Solution().findOrder(numCourses, prerequisites) in output

    print("-------")
    numCourses = 4
    prerequisites = [[1, 0], [2, 0], [3, 1], [3, 2]]

    output = [[0, 1, 2, 3], [0, 2, 1, 3]]

    assert Solution().findOrder(numCourses, prerequisites) in output
    print("-------")

    numCourses = 1
    prerequisites = []

    output = [[0]]

    assert Solution().findOrder(numCourses, prerequisites) in output
