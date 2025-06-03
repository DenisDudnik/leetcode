# https://leetcode.com/problems/letter-tile-possibilities/


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        result = 0
        tiles = sorted(tiles)

        def backtrack(path: list[str]):
            nonlocal result
            if path:
                result += 1
            for i in range(len(tiles)):
                if tiles[i] == "." or i>0 and tiles[i] == tiles[i-1]:
                    continue
                path.append(tiles[i])
                tmp, tiles[i] = tiles[i], "."
                backtrack(path)
                tiles[i] = tmp
                path.pop()

        backtrack([])
        return result


if __name__ == "__main__":
    solution = Solution()

    def check_case(tiles: str, expected: int):
        result = solution.numTilePossibilities(tiles)
        assert result == expected, f"Failed for input: {tiles}\nExpected: {expected}\nGot: {result}"

    # Пример 1
    check_case("AAB", 8)

    # Пример 2
    check_case("AAABBC", 188)

    # Пример 3
    check_case("V", 1)

    print("All test cases passed.")
