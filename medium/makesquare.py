# https://leetcode.com/problems/matchsticks-to-square/

from typing import List


class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if len(matchsticks) < 4:
            return False
        perimeter = sum(matchsticks)
        if perimeter % 4 > 0:
            return False

        matchsticks.sort(reverse=True)
        side_size = perimeter // 4
        sides = [0] * 4

        def backtrack(index: int) -> bool:
            if index == len(matchsticks) and all(side == side_size for side in sides):
                return True

            for i in range(4):
                if i> 0 and sides[i-1] == sides[i]:
                    continue
                if sides[i] + matchsticks[index] <= side_size:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]

                if sides[i] == 0:
                    break

            return False

        return backtrack(0)


# 🧪 Тесты из условия задачи
if __name__ == "__main__":
    sol = Solution()

    # Пример 1: можно составить квадрат
    assert sol.makesquare([1, 1, 2, 2, 2]) is True, "Test case 1 failed"

    # Пример 2: нельзя составить квадрат
    assert sol.makesquare([3, 3, 3, 3, 4]) is False, "Test case 2 failed"

    print("All tests passed.")
