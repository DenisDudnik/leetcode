# https://leetcode.com/problems/count-numbers-with-unique-digits/


# class Solution:
#     def countNumbersWithUniqueDigits(self, n: int) -> int:
#         if n == 0:
#             return 1
#         digits = list(range(10))
#         used = [False] * 10
#         result = []

#         def backtrack(path: list[int]):
#             if len(path) == n:
#                 return
#             for i in digits:
#                 if not used[i] and not (path and path[0] == 0):
#                     used[i] = True
#                     path.append(i)
#                     result.append(1)
#                     backtrack(path)
#                     path.pop()
#                     used[i] = False

#         backtrack([])
#         return len(result)


class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1
        if n == 1:
            return 10

        total = 10
        product = 9

        for i in range(2, n+1):
            product *= (11-i)
            total += product

        return total

# ✅ Тесты из описания задачи
if __name__ == "__main__":
    sol = Solution()

    # Примеры из условия
    assert sol.countNumbersWithUniqueDigits(0) == 1  # только число 0
    assert sol.countNumbersWithUniqueDigits(1) == 10  # 0..9
    assert sol.countNumbersWithUniqueDigits(2) == 91  # проверено вручную
    assert sol.countNumbersWithUniqueDigits(3) == 739
    assert sol.countNumbersWithUniqueDigits(4) == 5275

    print("✅ Все тесты пройдены.")
