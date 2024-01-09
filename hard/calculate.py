# https://leetcode.com/problems/basic-calculator/


class Solution:
    def calculate(self, s: str) -> int:
        result, cur, sign, stack = 0, 0, 1, []
        for c in s:
            # digit
            if c.isdigit():
                cur = cur * 10 + int(c)
            # +-
            elif c in ("+", "-"):
                result += cur * sign
                cur = 0
                sign = 1 if c == "+" else -1
            # (
            elif c == "(":
                stack.append(result)
                stack.append(sign)
                result = 0
                sign = 1
            # )
            elif c == ")":
                result += cur * sign
                result *= stack.pop()
                result += stack.pop()
                sign = 1
                cur = 0
        result += cur * sign
        return result


if __name__ == "__main__":
    assert Solution().calculate("1 + 1") == 2
    assert Solution().calculate(" 2-1 + 2 ") == 3
    assert Solution().calculate("(1+(4+5+2)-3)+(6+8)") == 23
