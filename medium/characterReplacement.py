# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2026-01-01
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        char_cnt = {}
        left = mostf = 0

        for right in range(len(s)):
            char_cnt[s[right]] = char_cnt.get(s[right], 0) + 1
            mostf = max(mostf, char_cnt[s[right]])

            while right - left + 1 > mostf + k:
                char_cnt[s[left]] -= 1
                left += 1

            longest = max(longest, right - left + 1)

        return longest


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
