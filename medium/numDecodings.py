# https://leetcode.com/problems/decode-ways/

# 2026-05-04
class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        prev1, prev2 = 1, 1

        for i in range(1, len(s)):
            current = 0
            if s[i] != "0":
                current += prev1

            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                current += prev2

            prev1, prev2 = current, prev1
        return prev1


def run_tests():
    sol = Solution()

    # базовые примеры
    assert sol.numDecodings("12") == 2  # "AB", "L"
    assert sol.numDecodings("226") == 3  # "BZ", "VF", "BBF"

    # нули (ключевые кейсы)
    assert sol.numDecodings("0") == 0
    assert sol.numDecodings("06") == 0  # ведущий ноль — невалидно :contentReference[oaicite:1]{index=1}
    assert sol.numDecodings("10") == 1  # только "J"
    assert sol.numDecodings("20") == 1
    assert sol.numDecodings("30") == 0

    # смешанные случаи
    assert sol.numDecodings("11106") == 2
    assert sol.numDecodings("101") == 1
    assert sol.numDecodings("110") == 1

    # одиночные символы
    assert sol.numDecodings("1") == 1
    assert sol.numDecodings("9") == 1

    # большие комбинации
    assert sol.numDecodings("27") == 1  # "BG", но не "AA"
    assert sol.numDecodings("26") == 2
    assert sol.numDecodings("2101") == 1

    # длинная строка
    assert sol.numDecodings("111111") == 13

    assert sol.numDecodings("2611055971756562") == 4

    print("Все тесты пройдены!")


if __name__ == "__main__":
    run_tests()
