# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, return the longest palindromic substring in s.
# Constraints:

# 1 <= s.length <= 1000
# s consist of only digits and English letters.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def isPalindrome(substring: str) -> bool:
            left = substring[0:len(substring)//2]
            right = substring[len(substring) - len(left)::]
            return True if left == right[::-1] else False


        if len(s) < 2 or isPalindrome(s):
            return s
        palindroms = set()
        for i in range(len(s)):
            simbol = s[len(s) - i - 1]
            if s.count(simbol[i:]) > 0:
                candidate = s[s.index(simbol): len(s) - i]
                while candidate.count(simbol) > 0:
                    candidate = candidate[candidate.index(simbol):]
                    if isPalindrome(candidate):
                        palindroms.add(candidate)
                        break
                    else:
                        candidate = candidate.replace(simbol, '', 1)
        res = list(palindroms)
        res.sort(key=len)
        print(res)
        return res[-1] if res else None


if __name__ == "__main__":
    # assert Solution().longestPalindrome("babad") == "bab" or "aba"
    # assert Solution().longestPalindrome("cbbd") == "bb"
    # assert Solution().longestPalindrome("pwwp") == "pwwp"
    # assert Solution().longestPalindrome("pwawp") == "pwawp"
    # assert Solution().longestPalindrome("ac") == "a" or "c"
    # assert Solution().longestPalindrome("qwer") == "q" or "w" or "e" or "r"
    # assert Solution().longestPalindrome("pwqqwpotewrwet") == "tewrwet"
    # assert Solution().longestPalindrome("aacabdkacaa") == "aca"
    assert Solution().longestPalindrome("babadada") == "adada"

