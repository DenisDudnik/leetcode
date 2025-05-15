# https://leetcode.com/problems/additive-number/


class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)

        def backtrack(start: int, path: list[int]) -> bool:
            if start == n and len(path) >= 3:
                return True

            for end in range(start + 1, n + 1):
                current = num[start:end]
                if len(current) > 1 and current[0] == "0":
                    break
                cur_num = int(current)
                if len(path) >= 2:
                    if cur_num < path[-2] + path[-1]:
                        continue
                    if cur_num > path[-2] + path[-1]:
                        break
                path.append(cur_num)
                if backtrack(end, path):
                    return True
                path.pop()
            return False

        return backtrack(0, [])


# class Solution:
#     def isAdditiveNumber(self, num: str) -> bool:
#         def backtrack(start: int, path: list[str]) -> bool:
#             if start == len(num) and len(path) >= 3:
#                 return True

#             for end in range(start + 1, len(num) + 1):
#                 current = num[start:end]
#                 # Пропуск чисел с лидирующим нулем (кроме "0")
#                 if len(current) > 1 and current[0] == "0":
#                     break
#                 if len(path) >= 2:
#                     if int(current) != int(path[-1]) + int(path[-2]):
#                         continue
#                 if backtrack(end, path + [current]):
#                     return True
#             return False

#         return backtrack(0, [])


# 🔽 Тесты из условия
assert Solution().isAdditiveNumber("112358") is True  # 1, 1, 2, 3, 5, 8
assert Solution().isAdditiveNumber("199100199") is True  # 1, 99, 100, 199

# 🔽 Дополнительные случаи
assert Solution().isAdditiveNumber("123") is True  # 1, 2, 3
assert Solution().isAdditiveNumber("1023") is False  # leading zero
assert Solution().isAdditiveNumber("000") is True  # 0, 0, 0
