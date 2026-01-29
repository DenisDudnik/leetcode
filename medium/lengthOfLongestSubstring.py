# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# 2026-01-29
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = max_len = 0
        ch_map = {}

        for right, ch in enumerate(s):
            if ch in ch_map and ch_map[ch] >= left:
                left = ch_map[ch] + 1
            max_len = max(max_len, right - left + 1)
            ch_map[ch] = right

        return max_len


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
    assert Solution().lengthOfLongestSubstring("abba") == 2
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
