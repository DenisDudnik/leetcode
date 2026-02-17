# https://leetcode.com/problems/longest-palindromic-substring/

# 2026-02-17
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def extend(l: int, r: int):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return l + 1, r - 1

        l = r = 0
        for i in range(len(s)):
            l1, r1 = extend(i, i)
            l2, r2 = extend(i, i + 1)
            if r1 - l1 > r - l:
                l, r = l1, r1
            if r2 - l2 > r - l:
                l, r = l2, r2

        return s[l : r + 1]


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
