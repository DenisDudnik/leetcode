# https://leetcode.com/problems/longest-palindromic-substring/

# 2026-01-18
class Solution:
    def longestPalindrome(self, s: str) -> str:
        left, right = 0, 0
        n = len(s)

        def extend(left: int, right: int):
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            return left + 1, right - 1

        for i in range(n):
            l1, r1 = extend(i, i)
            l2, r2 = extend(i, i + 1)

            if right - left <= r1 - l1:
                left, right = l1, r1
            if right - left <= r2 - l2:
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
