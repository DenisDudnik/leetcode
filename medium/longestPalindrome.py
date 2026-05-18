# https://leetcode.com/problems/longest-palindromic-substring/

# 2026-05-18
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(i: int, j: int):
            while i >= 0 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return i + 1, j - 1

        left, right = 0, 0

        for i in range(len(s)):
            l1, r1 = extend(i, i)
            l2, r2 = extend(i, i + 1)

            if r1 - l1 > right - left:
                left, right = l1, r1
            if r2 - l2 > right - left:
                left, right = l2, r2

        return s[left : right + 1]


if __name__ == "__main__":
    assert Solution().longestPalindrome("babad") == "bab" or "aba"
    assert Solution().longestPalindrome("cbbd") == "bb"
    assert Solution().longestPalindrome("pwwp") == "pwwp"
    assert Solution().longestPalindrome("pwawp") == "pwawp"
    assert Solution().longestPalindrome("ac") == "a" or "c"
    assert Solution().longestPalindrome("qwer") == "q" or "w" or "e" or "r"
    assert Solution().longestPalindrome("pwqqwpotewrwet") == "tewrwet"
    assert Solution().longestPalindrome("aacabdkacaa") == "aca"
    assert Solution().longestPalindrome("babadada") == "adada"
