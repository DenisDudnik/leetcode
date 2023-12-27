# https://leetcode.com/problems/is-subsequence/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        if not s:
            return True
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                if i == len(s) - 1:
                    return True
                i += 1
            j += 1
        return False


if __name__ == "__main__":
    assert Solution().isSubsequence(s="abc", t="ahbgdc") == True
    assert Solution().isSubsequence(s="axc", t="ahbgdc") == False
    assert Solution().isSubsequence(s="", t="ahbgdc") == True
