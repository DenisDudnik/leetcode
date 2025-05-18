# https://leetcode.com/problems/beautiful-arrangement/


class Solution:
    def countArrangement(self, n: int) -> int:
        result = 0
        used = [False] * (n+1)

        def backtrack(path_len: int):
            nonlocal result
            if path_len == n:
                result += 1
                return

            for num in range(1, n+1):
                if not used[num] and (num % (path_len + 1) == 0 or (path_len + 1) % num == 0):
                    used[num] = True
                    backtrack(path_len + 1)
                    used[num] = False

        backtrack(0)
        return result


# Примеры из условия задачи + дополнительный тест
if __name__ == "__main__":
    solution = Solution()

    # Пример 1
    n1 = 2
    expected1 = 2
    assert solution.countArrangement(n1) == expected1, "Test case 1 failed"

    # Пример 2
    n2 = 1
    expected2 = 1
    assert solution.countArrangement(n2) == expected2, "Test case 2 failed"

    # Дополнительный пример
    n3 = 3
    expected3 = 3
    assert solution.countArrangement(n3) == expected3, "Test case 3 failed"

    print("All test cases passed.")
