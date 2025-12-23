# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# 2025-12-23
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = left = 0
        char_map = {}

        for i, c in enumerate(s):
            if c in char_map and char_map[c] >= left:
                left = char_map[c] + 1

            char_map[c] = i
            result = max(result, i - left + 1)

        return result


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
    assert Solution().lengthOfLongestSubstring("abba") == 2
