# https://leetcode.com/problems/split-array-into-fibonacci-sequence/

from typing import List


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = []

        def backtrack(nums: str, path: list[int]) -> bool:
            if len(path) >= 3 and path[-3] + path[-2] != path[-1]:
                return False
            if not len(nums) and len(path) >= 3:
                result.extend(path[:])
                return True
            max_int = 2**31 - 1
            for i in range(1, len(nums) + 1):
                if i > 1 and nums[0] == "0":
                    break
                current = int(nums[0:i])
                if current > max_int:
                    break
                path.append(current)
                if backtrack(nums[i:], path):
                    return True
                path.pop()
            return False

        backtrack(num, [])
        return result


if __name__ == "__main__":
    solution = Solution()

    def check_case(s: str, expected: List[int]):
        result = solution.splitIntoFibonacci(s)
        assert result == expected, f"Failed for input: {s}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case("1101111", [11, 0, 11, 11])

    # Пример 2
    check_case("11235813", [1, 1, 2, 3, 5, 8, 13])

    # Пример 3
    check_case("0123", [])  # ведущие нули — недопустимо

    # Пример 4
    check_case("0000", [0, 0, 0, 0])

    # Пример 5
    check_case("539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511", [])

    print("All test cases passed.")

# [539834657,21,539834678,539834699,1079669377,1619504076,2699173453,4318677529,7017850982,11336528511]
