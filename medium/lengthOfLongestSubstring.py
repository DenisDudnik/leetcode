# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# 2026-04-04
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        left = 0
        idxs = {}

        for i, ch in enumerate(s):
            if ch in idxs and idxs[ch] >= left:
                left = idxs[ch] + 1
            idxs[ch] = i
            longest = max(longest, i - left + 1)

        return longest


if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
    assert Solution().lengthOfLongestSubstring("a") == 1
    assert Solution().lengthOfLongestSubstring("au") == 2
    assert Solution().lengthOfLongestSubstring("abba") == 2
    assert Solution().lengthOfLongestSubstring("dvdf") == 3
