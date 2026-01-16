# https://leetcode.com/problems/longest-palindromic-substring/

# 2026-01-16
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def extend(l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        for i in range(len(s)):
            l1, r1 = extend(i, i + 1)
            l2, r2 = extend(i, i)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start : end + 1]


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
