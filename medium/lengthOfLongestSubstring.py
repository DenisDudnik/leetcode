# https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Given a string s, find the length of the longest substring without repeating characters.
# Constraints:

# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)
        max_len = 0
        simbols = []
        for simbol in s:
            if simbols and simbol in simbols:
                max_len = max(max_len, len(simbols))
                simbols = simbols[simbols.index(simbol):]
                simbols.pop(0)
            simbols.append(simbol)
        max_len = max(max_len, len(simbols))
        return max_len


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
