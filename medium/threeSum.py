# https://leetcode.com/problems/3sum/

from typing import List


# 2026-01-01
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            target = -nums[i]
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[left] + nums[right] == target:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif nums[left] + nums[right] < target:
                    left += 1
                else:
                    right -= 1

        return result


# --------------------------
# ТЕСТЫ
# --------------------------


def check(result, expected):
    """
    Сравнение без учета порядка элементов и порядка троек.
    Каждая тройка сортируется, затем весь список сортируется.
    """
    r = sorted([sorted(x) for x in result])
    e = sorted([sorted(x) for x in expected])
    assert r == e, f"expected={e}, got={r}"


tests = [
    # БАЗОВЫЕ
    {
        "input": [-1, 0, 1, 2, -1, -4],
        "expected": [[-1, -1, 2], [-1, 0, 1]],
    },
    {
        "input": [0, 1, 1],
        "expected": [],
    },
    {
        "input": [0, 0, 0],
        "expected": [[0, 0, 0]],
    },
    # ДОПОЛНИТЕЛЬНЫЕ
    {
        "input": [3, -2, 1, 0],
        "expected": [],
    },
    {
        "input": [-2, 0, 1, 1, 2],
        "expected": [[-2, 0, 2], [-2, 1, 1]],
    },
    {
        "input": [-4, -2, -2, -2, 0, 1, 2, 2, 2, 4, 4],
        "expected": [[-4, 0, 4], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]],
    },
    # ЭКСТРЕМАЛЬНЫЕ
    {
        "input": [],
        "expected": [],
    },
    {
        "input": [0],
        "expected": [],
    },
    {
        "input": [0, 0],
        "expected": [],
    },
    {
        "input": [1, -1],
        "expected": [],
    },
    # МНОГО НУЛЕЙ
    {
        "input": [0] * 20,
        "expected": [[0, 0, 0]],
    },
    # МНОГО ДУБЛЕЙ
    {
        "input": [-1, -1, -1, 2, 2, 2, -1, 0, 1],
        "expected": [[-1, -1, 2], [-1, 0, 1]],
    },
]


# --------------------------
# ЗАПУСК ТЕСТОВ
# --------------------------
sol = Solution()

for t in tests:
    try:
        check(sol.threeSum(t["input"]), t["expected"])
    except NotImplementedError:
        print("Метод threeSum ещё не реализован — тесты не запускались.")
        break
    except AssertionError as e:
        print("Тест провален:", e)
        break
else:
    print("Все тесты пройдены!")
