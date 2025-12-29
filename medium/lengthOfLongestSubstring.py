# https://leetcode.com/problems/longest-substring-without-repeating-characters/


# 2025-12-29
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = left = 0
        idxs = {}

        for i in range(len(s)):
            if s[i] in idxs and idxs[s[i]] >= left:
                left = idxs[s[i]] + 1
            idxs[s[i]] = i
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
