# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1:
            return False
        brackets = []
        same = {
            ')': '(',
            ']': '[',
            '}': '{'
        }
        for c in s:
            if c in same:
                if (not brackets) or (brackets.pop() != same[c]):
                    return False
            else:
                brackets.append(c)
        return not brackets


if __name__ == "__main__":
    assert Solution().isValid("()") == True
    assert Solution().isValid("()[]{}") == True
    assert Solution().isValid("(]") == False
