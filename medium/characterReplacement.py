# https://leetcode.com/problems/longest-repeating-character-replacement/

# 2026-01-16
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        mostf = 0
        longest = 0
        ch_counts = {}

        for right, ch in enumerate(s):
            ch_counts[ch] = ch_counts.get(ch, 0) + 1
            mostf = max(mostf, ch_counts[ch])

            while right - left + 1 > mostf + k:
                ch_counts[s[left]] -= 1
                left += 1

            longest = max(right - left + 1, longest)

        return longest


# tests
s = Solution()
assert s.characterReplacement("ABAB", 2) == 4
assert s.characterReplacement("AABABBA", 1) == 4
assert s.characterReplacement("AAAA", 2) == 4
assert s.characterReplacement("ABCDE", 1) == 2
assert s.characterReplacement("BAAA", 1) == 4
assert s.characterReplacement("BAAAB", 2) == 5
