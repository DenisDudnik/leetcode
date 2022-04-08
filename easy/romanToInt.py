class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        res = []
        for item in s:
            if res and res[-1] < roman_dict.get(item, 0):
                res[-1] *= -1
            res.append(roman_dict.get(item, 0))
        # print(res)
        return sum(res)


if __name__ == "__main__":
    assert Solution().romanToInt("III") == 3
    assert Solution().romanToInt("LVIII") == 58
    assert Solution().romanToInt("MCMXCIV") == 1994
    assert Solution().romanToInt("MRMXCIV") == 2094
    assert Solution().romanToInt("") == 0
