# https://leetcode.com/problems/longest-palindromic-substring/

# 2026-01-12
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, end = 0, 0

        def expand(left: int, right: int):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(len(s)):
            l1, r1 = expand(i, i)
            l2, r2 = expand(i, i + 1)

            if r1 - l1 > end - start:
                start, end = l1, r1

            if r2 - l2 > end - start:
                start, end = l2, r2

        return s[start: end + 1]


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
