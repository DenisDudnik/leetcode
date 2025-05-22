# https://leetcode.com/problems/restore-ip-addresses/

from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        if len(s) < 4 or len(s) > 12:
            return []

        result = []
        n = len(s)

        def backtrack(index: int, path: list[str]):
            # break bad cases
            if len(path) > 0 and (
                len(path) > 4
                or len(s[index:]) / 3 > 4 - len(path)
                or (len(path[-1]) > 1 and path[-1][0] == "0")
                or (len(path[-1]) and int(path[-1]) > 255)
            ):
                return
            # save good cases
            if index == n and len(path) == 4:
                result.append(".".join(path))
                return
            backtrack(index + 1, path + [s[index : index + 1]])
            backtrack(index + 2, path + [s[index : index + 2]])
            backtrack(index + 3, path + [s[index : index + 3]])

        backtrack(0, [])
        return result


# Примеры из условия задачи и граничные случаи
if __name__ == "__main__":
    solution = Solution()

    def check_case(s: str, expected: List[str]):
        result = solution.restoreIpAddresses(s)
        assert sorted(result) == sorted(expected), f"Failed for input: {s}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case("25525511135", ["255.255.11.135", "255.255.111.35"])

    # Пример 2
    check_case("0000", ["0.0.0.0"])

    # Пример 3
    check_case("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"])

    # Пример 4
    check_case("000256", [])

    # Пример 5
    check_case(
        "172162541", ["17.216.25.41", "17.216.254.1", "172.16.25.41", "172.16.254.1", "172.162.5.41", "172.162.54.1"]
    )

    # Длина < 4 (невозможно сформировать IP)
    check_case("123", [])

    # Длина > 12 (невозможно сформировать IP)
    check_case("1234567890123", [])

    print("All test cases passed.")
