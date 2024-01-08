# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token not in ("+", "-", "*", "/"):
                stack.append(int(token))
            else:
                y = stack.pop()
                x = stack.pop()
                if token == "+":
                    stack.append(x + y)
                elif token == "-":
                    stack.append(x - y)
                if token == "*":
                    stack.append(x * y)
                if token == "/":
                    stack.append(int(x / y))
        return stack[0]


if __name__ == "__main__":
    assert Solution().evalRPN(["2", "1", "+", "3", "*"]) == 9
    assert Solution().evalRPN(["4", "13", "5", "/", "+"]) == 6
    assert Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]) == 22
