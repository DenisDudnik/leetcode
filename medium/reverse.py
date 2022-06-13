# https://leetcode.com/problems/reverse-integer/

# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer range [-2**31, 2**31 - 1], then return 0.

class Solution:
    def reverse(self, x: int) -> int:
        value = abs(x)
        digit = 1 if value == x else -1
        res = 0
        while value > 0:
            if res >= -2 ** 31 / 10 and res <= (2 ** 31 - 1) / 10:
                res = res * 10 
                if -2 ** 31 - res <= digit * (value % 10) or 2 ** 31 - 1 - res >= digit * (value % 10):
                    res += digit * (value % 10)
                    value //= 10
                else:
                    return 0
            else:
                return 0
        return res


if __name__ == "__main__":
    assert Solution().reverse(x = 123) == 321
    assert Solution().reverse(x = -123) == -321
    assert Solution().reverse(x = 120) == 21
    assert Solution().reverse(x = -2 ** 31) == 0
    assert Solution().reverse(x = 2 ** 31 + 1) == 0
    assert Solution().reverse(x = 7463847412) == 2147483647
    assert Solution().reverse(x = -8463847412) == -2147483648
    # -2147483648 <= x <= 2147483648 - 1